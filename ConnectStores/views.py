from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def article(request):
    return  HttpResponse("vue pour les articles")

def panier(request):
    return HttpResponse("vue du panier")

def categorie(request):
    return HttpResponse("vue des categorie")

def client(request):
    return  HttpResponse("vue des clients")