# Generated by Django 5.2.3 on 2025-07-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_listareproduccion_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancion',
            name='lista',
        ),
        migrations.AddField(
            model_name='listareproduccion',
            name='canciones',
            field=models.ManyToManyField(blank=True, related_name='listas', to='core.cancion'),
        ),
    ]
