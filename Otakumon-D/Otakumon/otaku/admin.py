from django.contrib import admin
from .models import Editorial
from .models import Autor
from .models import Manga
from .models import MangaInicio

# Register your models here.

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Manga)
admin.site.register(MangaInicio)