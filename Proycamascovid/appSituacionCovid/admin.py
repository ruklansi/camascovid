from django.contrib import admin

# Register your models here.
from .models import personas_covid

from .models import hospitales

from .models import camas_hospitales


class personas(admin.ModelAdmin):
    list_display = ('fecha_personas', 'fuerza', 'activos', 'recuperados', 'sospechosos', 'fallecidos')

admin.site.register(personas_covid, personas)

class camas(admin.ModelAdmin):
    list_display = ('fecha_cama', 'camas_ocupadas', 'camas_libres', 'hospital')

admin.site.register(camas_hospitales, camas)

class hospitalmil(admin.ModelAdmin):
    list_display = ('hospital', 'region', 'fuerza')
admin.site.register(hospitales, hospitalmil)