from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def somma(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    var1= random.randint(1,10)
    var2= random.randint(1,10)
    somma = var1 + var2
    dic = { 'var1': var1,
        'var2': var2,
        'somma': somma }
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render (request, "somma.html", dic)

def media(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    list2=[]
    somma=0
    for i in range (30): 
        list2.append(random.randint(1,10))
        somma+=list2[i]
    media=somma/30
    dic = { 'list2': list2, 'media': media,}
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render (request, "media.html", dic)

def voti(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    list2=[]
    for i in range (30): 
        list2[i]=random.randint(1,10)
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render (request, "voti.html", list2)