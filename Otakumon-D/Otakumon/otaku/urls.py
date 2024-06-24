from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('mangas/<str:item_nombre>/', views.mangas, name="mangas"),
    path('detalles/<str:item_id>/', views.detalles, name="detalles")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)