from django import forms
from .models import *
from django.contrib.auth.models import User


class PridatRecept(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ('jmeno', 'ingredience', 'postup', 'svetova_kuchyne', 'chod',)
        fotka = forms.ImageField()


class PridatKomentar(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ('nadpis', 'text',)


class HodnoceniReceptu(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ('hodnoceni',)


class OdeslatZpravu(forms.ModelForm):
    class Meta:
        model = Zprava
        fields = ('nadpis', 'text', 'odesilatel',)


class PridatClanek(forms.ModelForm):
    class Meta:
        model = Clanek
        fields = ('nadpis', 'text',)

