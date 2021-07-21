from django.db import models
from django.conf import settings


class Balance(models.Model):
    amount = models.IntegerField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Balance for {self.user.first_name} {self.user.last_name}'
