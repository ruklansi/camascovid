from django.db import models
from django.contrib import admin
# Create your models here now.

class personas_covid(models.Model):
    FUERZAS = (
        (1, 'EA'),
        (2, 'FAA'),
        (3, 'ARA'),
    )

    semana = models.IntegerField(blank=True, null=True, default=0)
    fecha = models.DateField(blank=True, null=True)
    fuerza = models.PositiveSmallIntegerField(choices=FUERZAS, null=True, blank=True)
    activos = models.IntegerField(blank=True, null=True, default=0)
    recuperados = models.IntegerField(blank=True, null=True, default=0)
    sospechosos = models.IntegerField(blank=True, null=True, default=0)
    fallecidos = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name_plural = "Situación Sanitaria - Personal Militar Actividad "

    def __str__(self):
        return str(self.semana)

class hospitales(models.Model):
    REGION = (
        (1, 'AMBA'),
        (2, 'INTERIOR'),
    )
    FFAA = (
        (1, 'EA'),
        (2, 'FAA'),
        (3, 'ARA'),
    )

    semana = models.IntegerField(blank=True, null=True, default=0)
    hospital = models.CharField(max_length=50)
    total_de_camas = models.IntegerField(blank=True, null=True)
    region = models.PositiveSmallIntegerField(choices=REGION, null=True, blank=True)
    fuerza = models.PositiveSmallIntegerField(choices=FFAA, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Hospitales"
        
    def __str__(self):
        return self.hospital

class camas_hospitales(models.Model):
    SITCAMAS = (
        (1, 'CRITICAS'),
        (2, 'INTERMEDIAS'),
        (3, 'AISLAMIENTO')
    )

    camas_libres = models.IntegerField(blank=True, null=True, default=0)
    hospital = models.ForeignKey(hospitales, blank=True, null=True, on_delete=models.CASCADE)
    situacion = models.PositiveSmallIntegerField(choices=SITCAMAS, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Camas Hospitales"

    def __str__(self):
        return str(self.camas_libres)

class role_inline(admin.TabularInline):
    model = camas_hospitales
    extra = 1

