# Generated by Django 3.2.13 on 2022-05-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSituacionCovid', '0017_auto_20220506_0857'),
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