import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
'''from django.http import HttpResponse
from.models import Articolo, Giornalista
def home (request):
a =
g =
for art in Articolo.objects.all():
    a += (art.titolo + "<br>")
for gio in Giornalista.objects.all():
    g+= (gio.nome + "<br>")
response = "Articoli: <br>"+a+ "<br>Giornalisti: <br>" + g
return HttpResponse("<h1>" + response + "</h1>")
'''
# Create your views here.
'''def home (request):
    a = []
    g = [] 
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all(): 
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)
    return HttpResponse("<h1>" + response + "</h1>")
'''


def home (request):
    articoli= Articolo.objects.all()
    giornalisti =Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render (request, "news/homepage.html", context)
def articoloDetailViews (request, pk):
    articolo= get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render (request, "articolo_detail.html", context)

def listaArticoli (request, pk=None):
    if pk==None:
        articoli = Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context= {
        'articoli': articoli,
    }
    return render (request, 'lista_articoli.html', context)

def queryBase(request):
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')
    numero_totale_articoli = Articolo.objects.count()
    giornalista_1 = Giornalista.objects.get(id=2)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()
    ultimi = Articolo.objects.order_by('-data')[:5]
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()
    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__lte=visualizzazioni))
    articoli_con_not = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)
    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'giornalista_1': giornalista_1,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'giornalisti_nati': giornalisti_nati,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'articoli_mese_anno': articoli_mese_anno,
        'giornalisti_con_articoli_popolari': giornalisti_con_articoli_popolari,
        'data': data,
        'visualizzazioni': visualizzazioni,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not,
    }
    return render(request, "query.html", context)