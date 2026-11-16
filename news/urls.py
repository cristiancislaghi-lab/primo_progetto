from django.urls import path
from .views import home, articoloDetailViews, listaArticoli

app_name ='news'

urlpatterns = [
    path('', home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailViews, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("lista_articoli", listaArticoli, name="lista_articoli")
]