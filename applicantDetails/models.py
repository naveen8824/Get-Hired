from django.db import models
from users.models import User
from recruiter.models import Jobs

# Create your models here.

class ApplicantDetails (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True , blank=True)
    last_name = models.CharField(max_length=100, null=True , blank=True)
    city = models.CharField(max_length=100, null=True , blank=True)
    state = models.CharField(max_length=100, null=True , blank=True)
    country = models.CharField(max_length=100, null=True , blank=True)
    # resume = models.FileField

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class JobApplications (models.Model):
    job = models.ForeignKey(Jobs , on_delete=models.CASCADE , related_name='+')
    applicant = models.ForeignKey(User , on_delete=models.CASCADE , related_name='+')