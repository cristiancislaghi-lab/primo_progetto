from django.shortcuts import render
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
    return render (request, "homepage.html", context)