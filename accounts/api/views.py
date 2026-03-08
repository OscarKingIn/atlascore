from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from tenants.models import Client, Domain
from accounts.models import User
from django_tenants.utils import tenant_context

from .signup_serializer import SignupSerializer

# Current User Endpoint
def get(request):
    user = request.user

    return Response({
        "id": user.id,
        "email": user.email,
        "is_staff": user.is_staff
    })


class MeView(APIView):

    permission_classes = [IsAuthenticated]


# Tenant Signup Endpoint
def post(request):

    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data

    schema_name = data["domain"].replace(".", "_")

    tenant = Client.objects.create(
        schema_name=schema_name,
        name=data["company_name"]
    )

    Domain.objects.create(
        domain=data["domain"],
        tenant=tenant,
        is_primary=True
    )

    # Create admin user inside tenant schema
    with tenant_context(tenant):

        User.objects.create_superuser(
            email=data["email"],
            password=data["password"]
        )

    return Response(
        {"message": "Tenant created successfully"},
        status=status.HTTP_201_CREATED
    )


class SignupView(APIView):

    permission_classes = []

