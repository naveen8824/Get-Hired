from django import forms
from .models import ApplicantDetails

class ApplicantDetailsForm(forms.ModelForm):
    class Meta:
        model = ApplicantDetails
        fields= ['first_name' , 'last_name' , 'city' , 'state' , 'country','cv']