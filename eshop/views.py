from django.shortcuts import render
from .models import Kniha, Zanr, Autor

# Create your views here.
# Pohled pro zobrazení domovské stránky
def index(request):
    #zanr = 'povídky'
    context = {
        'nadpis': 'Knihy',
        'knihy': Kniha.objects.order_by('rok_vydani'),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)

def zanry(request):
    context = {
        'nadpis' : 'Seznam žánrů',
        'zanry' : Zanr.objects.all()

    }
    return render(request, 'zanry.html', context=context)


def zanr_detail(request, pk):
    zanr = Zanr.objects.get(id=pk)
    context = {
        'nadpis' : zanr,
        'knihy' : Kniha.objects.filter(zanry=zanr)
    }
    return render(request, 'zanr_detail.html', context=context)

def autori(request):
    context = {
        'nadpis' : 'Seznam autorů',
        'autori' : Autor.objects.all()
    }
    return render(request, 'autori.html', context=context)

def autor_detail(request, pk):
    autor = Autor.objects.get(id=pk)
    context = {
        'autor' : autor,
        'knihy' : Kniha.objects.filter(autori=autor)
    }
    return render(request, 'autor_detail.html', context=context)

def knihy(request):
    context = {
        'nadpis' : 'Seznam knih',
        'knihy' : Kniha.objects.order_by('autori')
    }
    return render(request, 'knihy.html', context=context)

def kniha_detail(request, pk):
    kniha = Kniha.objects.get(id=pk)
    context = {
        'kniha' : kniha,
        'autori' : kniha.autori
    }
    return render(request, 'kniha_detail.html', context=context)
