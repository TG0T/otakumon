from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login
from .models import Manga
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm, IngresoManga
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
# Create your views here.


def index(request):
    filtro = ['hxh1','sxf1','jjk1','sbd1','ksc1','yac1','aot1','csm1','sld1','tkr1','kny1','fma1'] #filtra ids
    mangas = Manga.objects.filter(id__in=filtro) #llamamos objeto y utilizamos el filtro
    return render(request, "otaku/index.html", {"mangas": mangas})

def mangas(request, item_nombre):
    listamanga = Manga.objects.all()
    mangas = Manga.objects.filter(nombre=item_nombre)  # Filtra por nombre
    return render(request, "otaku/mangas.html", {'mangas': mangas, 'listamanga': listamanga})

def detalles(request, item_id):
    listamanga = Manga.objects.all()
    detalle = get_object_or_404(Manga, id=item_id)
    return render(request, "otaku/detalles.html", {'detalle': detalle, 'listamanga': listamanga})

def logout_view(request):
    messages.success(request, "Has cerrado sesión Correctamente!")
    logout(request)
    return redirect('index')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.success(request, "Usuario Correctamente!")

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('index')

    return render(request, 'registration/register.html', data)


def ingresomanga(request):
    context = {
        'form': IngresoManga()
    }

    if request.method == 'POST':
        manga_form = IngresoManga(data=request.POST, files=request.FILES)
        if manga_form.is_valid():
            manga_form.save()
            messages.success(request, "Ingresado Correctamente!")
            return redirect('listar_mangas')
        else:
            context["form"] = manga_form

    return render(request, 'otaku/ingreso_manga.html', context)

def listar_mangas(request):
    mangas = Manga.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mangas, 10)
        mangas = paginator.page(page)
    except InvalidPage:
        raise Http404

    data = {
        'entity': mangas,
        'paginator': paginator
    }

    return render(request, 'otaku/listamanga.html', data)

def edit(request, id_manga):
    manga = Manga.objects.get(id=id_manga)
    if request.method == 'POST':
        form = IngresoManga(request.POST, request.FILES, instance=manga)
        if form.is_valid():
            form.save()
            return redirect('listar_mangas')
    else:
        form = IngresoManga(instance=manga)
    return render(request, "otaku/mangaedit.html", {'form': form, 'manga': manga})

def actualiza(request, id_manga):
    manga = get_object_or_404(Manga, pk=id_manga)

    data = {
        'form' : IngresoManga(instance=manga),
        'manga' : manga
    }
    if request.method == 'POST':
        formulario = IngresoManga(data=request.POST, instance=manga, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to='listar_mangas')
        data['form'] = formulario

    return render(request, 'otaku/mangaedit.html', data, {'messages': messages.get_messages(request)})

def delete (request, id_manga):
    manga = Manga.objects.get(pk = id_manga)
    manga.delete()
    messages.success(request, "Eliminado Correctamente!")
    mangas = Manga.objects.all()

    return render(request, 'otaku/listamanga.html', {'mangas' : mangas})