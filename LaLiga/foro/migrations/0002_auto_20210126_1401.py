# Generated by Django 3.0.3 on 2021-01-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]