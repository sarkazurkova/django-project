from django.shortcuts import render
from models import Kniha, Zanr

# Create your views here.
# Pohled pro zobrazení domovské stránky
def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)
