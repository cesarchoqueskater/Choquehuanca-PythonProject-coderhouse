from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    birth_date = models.DateField(null=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)