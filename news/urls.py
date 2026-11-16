from django.urls import path
from .views import home, articoloDetailViews

app_name ='news'

urlpatterns = [
    path('', home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailViews, name="articolo_detail")
]