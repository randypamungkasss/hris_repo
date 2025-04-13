from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.
class Departement(BaseModel):
    name = models.CharField(max_length=100)

class DepartementMember(BaseModel):
    departemnet = models.ForeignKey(Departement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
