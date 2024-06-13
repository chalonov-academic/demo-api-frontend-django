from django.db import models
from django import forms


class IdForm(forms.Form):
    numeroId = forms.IntegerField(label='Ingrese un id', required=True)


class IsbnForm(forms.Form):
    numeroIsbn = forms.IntegerField(label='Ingrese un ISBN', required=True)
