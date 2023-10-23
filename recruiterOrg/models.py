from django.db import models
from users.models import User


# Create your models here.

class Organization (models.Model):
    recruiter = models.OneToOneField(User , on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100 , null=True , blank=True)
    lob = models.CharField(max_length=100, null=True , blank=True)
    location = models.CharField(max_length=100, null=True , blank=True)

    def __str__(self):
        return self.org_name
    
