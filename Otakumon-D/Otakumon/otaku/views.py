from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "otaku/index.html")

def registro(request):
    return render(request, "otaku/registro.html")
