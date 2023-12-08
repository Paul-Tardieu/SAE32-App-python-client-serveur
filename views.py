from django.shortcuts import render, get_object_or_404
from .models import Colis, Evenement
from django.shortcuts import render
from .models import Colis, Evenement


def suivi_colis(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    evenements = Evenement.objects.filter(colis=colis).order_by('-date')
    return render(request, 'suivi_colis.html', {'colis': colis, 'evenements': evenements})


def enregistrer_evenement(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    description = "Colis en mouvement"  # À personnaliser selon vos besoins
    Evenement.objects.create(colis=colis, description=description)
    return render(request, 'enregistrement_evenement.html', {'colis': colis})