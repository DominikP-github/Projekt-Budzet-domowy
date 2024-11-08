# forms.py
from django import forms
from .models import Kategoria,tranzakcje

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'zysk']  # Dodajemy pole 'data'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Używamy widgetu 'date' do wyboru daty
        }

class PodkategoriaForm(forms.ModelForm):
    class Meta:
        model = tranzakcje
        fields = ['nazwa', 'plan', 'realizacja', 'saldo', 'data', 'kategoria','jednorazowa']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Używamy widgetu 'date' do wyboru daty
        }

class KategoriaForm2(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'zysk']  # Pola, które chcesz edytować w formularzu
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Ustawienie widgetu dla daty
        }

class KategoriaForm3(forms.ModelForm):
    class Meta:
        model = tranzakcje
        fields = ['nazwa', 'plan', 'realizacja', 'saldo', 'data', 'kategoria']  # Pola, które chcesz edytować w formularzu
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Ustawienie widgetu dla daty
        }