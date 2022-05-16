from django import forms
from esign.models import changerequest

class changerequestForm(forms.ModelForm):
    class Meta:
        model = changerequest
        fields = "__all__"