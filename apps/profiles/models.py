from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)