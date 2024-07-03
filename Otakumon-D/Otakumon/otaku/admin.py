from django.contrib import admin
from .models import Editorial
from .models import Autor
from .models import Manga, Boleta
from django.contrib.auth.models import Permission


# Register your models here.

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Manga)
admin.site.register(Permission)
admin.site.register(Boleta)