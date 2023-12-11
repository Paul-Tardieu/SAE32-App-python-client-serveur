from django.shortcuts import render, get_object_or_404
from .models import Colis, Evenement
from django.shortcuts import render
from .models import Colis, Evenement
from django.shortcuts import render
from . import forms


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', context={'form': form})
    

def suivi_colis(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    evenements = Evenement.objects.filter(colis=colis).order_by('-date')
    return render(request, 'pykorp/templates/suivi_colis.html', {'colis': colis, 'evenements': evenements})


def enregistrer_evenement(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    description = "Colis en mouvement"  # À personnaliser selon vos besoins
    Evenement.objects.create(colis=colis, description=description)
    return render(request, 'pykorp/templates/enregistrement_evenement.html', {'colis': colis})