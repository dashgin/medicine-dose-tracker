from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=120)
    dosage = models.CharField(max_length=120)
    frequency = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name
