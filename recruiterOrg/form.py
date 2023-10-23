from django import forms
from .models import Organization

class OrganizationDetails(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['org_name' , 'lob' , 'location']