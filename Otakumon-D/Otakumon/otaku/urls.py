from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

#localhost:8000/api/manga

urlpatterns = [
    path("", views.index, name="index"),
    path('mangas/<str:item_nombre>/', views.mangas, name="mangas"),
    path('detalles/<str:item_id>', views.detalles, name='detalles'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('ingreso_manga/', views.ingresomanga, name='ingresomanga'),
    path('listar_mangas/', views.listar_mangas, name='listar_mangas'),
    path('editar_manga/<str:id_manga>', views.edit, name='edit'),
    path('actualiza/<str:id_manga>', views.actualiza, name='actualiza'),
    path('eliminar/<str:id_manga>', views.delete, name='delete'),
    path('agregar_al_carrito/<str:manga_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito_detalle/', views.carrito_detalle, name='carrito_detalle'),
    path('eliminar_del_carrito/<str:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar_carrito/', views.actualizar_carrito, name='actualizar_carrito'),
    path('boleta/', views.boleta, name='boleta'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)