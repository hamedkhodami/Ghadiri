from django import forms
from .models import  Counseling


# Counseling form
class CounselingForm(forms.ModelForm):
    class Meta:
        model = Counseling
        fields = "__all__"
