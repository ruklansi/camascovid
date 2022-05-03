from django.contrib import admin

# Register your models here.
from .models import *

class personas(admin.ModelAdmin):
    list_display = ('semana', 'fecha', 'fuerza', 'activos', 'recuperados', 'sospechosos', 'fallecidos')

admin.site.register(personas_covid, personas)

# class camas(admin.ModelAdmin):
#     list_display = ('semana','camas_ocupadas', 'camas_libres', 'hospital', 'situacion')

# admin.site.register(camas_hospitales, camas)

class hospitalmil(admin.ModelAdmin):
    list_display = ('hospital', 'region', 'fuerza')
    inlines = (role_inline,)
admin.site.register(hospitales, hospitalmil)
    