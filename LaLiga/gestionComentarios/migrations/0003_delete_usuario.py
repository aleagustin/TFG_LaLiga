# Generated by Django 3.1.2 on 2021-01-09 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionComentarios', '0002_comentario_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]