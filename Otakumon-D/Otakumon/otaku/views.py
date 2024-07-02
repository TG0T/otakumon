from django.shortcuts import render, get_object_or_404
from .models import Manga
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    filtro = ['hxh1','sxf1','jjk1','sbd1','ksc1','yac1','aot1','csm1','sld1','tkr1','kny1','fma1'] #filtra ids
    mangas = Manga.objects.filter(id__in=filtro) #llamamos objeto y utilizamos el filtro
    return render(request, "otaku/index.html", {"mangas": mangas})

def registro(request):
    return render(request, "otaku/registro.html")

def mangas(request, item_nombre):
    listamanga = Manga.objects.all()
    mangas = Manga.objects.filter(nombre=item_nombre)  # Filtra por nombre
    return render(request, "otaku/mangas.html", {'mangas': mangas, 'listamanga': listamanga})

def detalles(request, item_id):
    listamanga = Manga.objects.all()
    detalle = get_object_or_404(Manga, id=item_id)
    return render(request, "otaku/detalles.html", {'detalle': detalle, 'listamanga': listamanga})

def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'mytest/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page?
            # return HttpResponseRedirect('/')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'mytest/login.html', {'context': context})    