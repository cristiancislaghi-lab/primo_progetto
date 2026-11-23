from django.urls import path
from .views import home, articoloDetailViews, listaArticoli, queryBase, giornalistaDetailView,listaGiornalisti, index_news

app_name ='news'

urlpatterns = [
    path('', home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailViews, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("query_base", queryBase, name="query_base"),
    path("giornalista_detail/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("giornalista_detail", giornalistaDetailView, name="giornalista_detail"),
    path("lista_giornalisti/<int:pk>", listaGiornalisti, name="lista_giornalisti"),
    path("lista_giornalisti", listaGiornalisti, name="lista_giornalisti"),
    path("index_news", index_news, name="index_news")
]