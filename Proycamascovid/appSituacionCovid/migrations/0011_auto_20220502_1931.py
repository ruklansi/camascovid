# Generated by Django 3.2.13 on 2022-05-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSituacionCovid', '0010_remove_personas_covid_fecha_personas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camas_hospitales',
            name='fecha_cama',
        ),
        migrations.AddField(
            model_name='camas_hospitales',
            name='Semana_camas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personas_covid',
            name='semana_persmil',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
