from django import forms

from .models import Walk


class WalkForm(forms.ModelForm):

    class Meta:
        model = Walk
        fields = ["weather", "steps", "startpoint","endpoint","content","image","user",]
        widgets = {
            "user": forms.HiddenInput()
        }