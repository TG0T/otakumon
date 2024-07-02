from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)