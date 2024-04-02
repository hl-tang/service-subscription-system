from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.username}"
