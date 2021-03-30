from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm, DomicilioForm
from .models import domicilio


def reserva(request):
    reserva = Reserva.objects.all()
    ctx={
        'reserva' : reserva,
    }
    return render(request, 'reserva.html', ctx)

def createReserva(request):
    if request.method == 'GET':
        form = ReservaForm()
        ctx = {
            'form': form
        }
    else:
        form = ReservaForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('Reserva')

    return render(request, 'manage_reserva.html', ctx)

def Domicilio(request):
    login = login.objects.all()
    ctx={
        'Domicilio': Domicilio,
    }
    return render(request, 'domicilio.html', ctx)

def createDomicilio(request):
    if request.method == 'GET':
        form = DomicilioForm()
        ctx = {
            'form': form
        }
    else:
        form = DomicilioForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('Domicilio')

    return render(request, 'manage_domicilio.html', ctx)
    
