from django.db import models
from users.models import User

# Create your models here.

class Jobs(models.Model):
    recruiter = models.ForeignKey(User , on_delete=models.CASCADE , related_name='+')
    jobTitle = models.CharField(max_length=100)
    jobDesc = models.CharField(max_length=500 )
    jobLocation = models.CharField(max_length=100)
    
