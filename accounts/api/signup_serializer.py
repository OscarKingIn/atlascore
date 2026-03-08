from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    company_name = serializers.CharField()
    domain = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)