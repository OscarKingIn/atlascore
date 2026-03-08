from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company_role = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Admin'),
            ('manager', 'Manager'),
            ('staff', 'Staff'),
        ],
        default='staff'
    )

    mfa_enabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username