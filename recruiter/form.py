from django import forms
from .models import Jobs

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['jobTitle' , 'jobDesc' , 'jobLocation']