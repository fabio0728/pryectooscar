from django import forms
from .models import Reserva
from .models import domicilio

class  ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class  DomicilioForm(forms.ModelForm):
    class Meta:
        model = domicilio
        fields = '__all__'