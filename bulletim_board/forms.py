from importlib.metadata import files
import os
from django import forms
from .models import bulletim_board
from django.core.mail import EmailMessage


class bulletim_boardCreateForm(forms.ModelForm):
    class Meta:
        model =bulletim_board
        fields =('title', 'content', 'photo1', 'photo2', 'photo3',)

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
