from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm, IngresoManga, FormularioItemCarrito
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from .models import Manga, ItemCarrito, Carrito, Boleta
import time
import datetime

#PAGINAS Y DETALLES
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

#CONTROL DE USUARIOS
def logout_view(request):
    time.sleep(1)
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

#CRUD
@permission_required('otaku.add_manga')
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

@permission_required('otaku.view_manga')
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

@permission_required('otaku.change_manga')
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
@permission_required('otaku.change_manga')
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
@permission_required('otaku.delete_manga')
def delete (request, id_manga):
    manga = Manga.objects.get(pk = id_manga)
    manga.delete()
    messages.success(request, "Eliminado Correctamente!")
    mangas = Manga.objects.all()

    return render(request, 'otaku/listamanga.html', {'mangas' : mangas})

#CARRITO DE COMPRAS
@login_required
def agregar_al_carrito(request, manga_id):
    manga = Manga.objects.get(id=manga_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, manga=manga)
    time.sleep(1)
    messages.success(request, "Añadido Correctamente!")
    if not created:
        item_carrito.cantidad += 1
        item_carrito.save()
    return redirect('carrito_detalle')

@login_required
def carrito_detalle(request):
    if Carrito.objects.filter(usuario=request.user).exists():
        carrito = Carrito.objects.get(usuario=request.user)
        items_carrito = ItemCarrito.objects.filter(carrito=carrito)
        total_carrito = sum(item.subtotal for item in items_carrito)
        return render(request, 'otaku/carrito_detalle.html', {'items_carrito': items_carrito, 'total_carrito': total_carrito})
    else:
        return render(request, 'otaku/carrito_detalle.html', {'items_carrito': [], 'total_carrito': 0})

@login_required
def eliminar_del_carrito(request, item_id):
    item_carrito = ItemCarrito.objects.get(id=item_id)
    item_carrito.delete()
    return redirect('carrito_detalle')

@login_required
def actualizar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    for item in items_carrito:
        form = FormularioItemCarrito(request.POST, instance=item)
        if form.is_valid():
            form.save()
    return redirect('carrito_detalle')

#BOLETA
def boleta(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    total_carrito = sum(item.cantidad * item.manga.precio for item in items_carrito)
    username = request.user.username
    email = request.user.email

    boleta = Boleta.objects.create(
        usuario=request.user,
        total_carrito=total_carrito,
    )

    # realiza el return
    try:
        return render(request, 'otaku/boleta.html', {
            'items_carrito': items_carrito,
            'total_carrito': total_carrito,
            'fecha_compra': datetime.date.today(),
            'numero_boleta': boleta.numero_boleta,
            'usuario' : username,
            'email' : email
        })
    finally: #limpia el carrito
        items_carrito.delete()