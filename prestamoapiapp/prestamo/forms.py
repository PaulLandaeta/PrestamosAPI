from django import forms
from .models import Credito


class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = "__all__"
