from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    isRecruiter = models.BooleanField(default=False)
    isApplicant = models.BooleanField(default=False)
    resumeUpdatedbyApplicant = models.BooleanField(default=False)
    orgUpdatedbyRecruiter = models.BooleanField(default=False) 

    
