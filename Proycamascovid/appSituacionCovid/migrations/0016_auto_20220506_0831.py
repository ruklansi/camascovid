# Generated by Django 3.2.13 on 2022-05-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSituacionCovid', '0015_hospitales_total_de_camas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camas_hospitales',
            name='semana',
        ),
        migrations.AddField(
            model_name='hospitales',
            name='semana',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
