from operator import mod
from pyexpat import model
from django import forms
from .models import *
from College.models import EventRegister

class StudentForm(forms.ModelForm):
    class Meta:
        model = EventRegister
        fields = "__all__"