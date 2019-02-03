from django.db import models

class Lead(models.Model):
    name = models.models.CharField(max_length=100)
    email = models.models.EmailField(max_length=100, unique=True)
    message = models.models.CharField(max_length=500, blank=True)
    created_at = models.models.DateTimeField(auto_now_add=True)
    