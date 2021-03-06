# Generated by Django 3.0.3 on 2021-01-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=255)),
                ('id_equipo', models.CharField(max_length=255)),
                ('nombre_equipo', models.CharField(max_length=255)),
                ('puntos', models.CharField(max_length=255)),
                ('pj', models.CharField(max_length=255)),
                ('pg', models.CharField(max_length=255)),
                ('pe', models.CharField(max_length=255)),
                ('pp', models.CharField(max_length=255)),
                ('gf', models.CharField(max_length=255)),
                ('gc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_partido', models.CharField(max_length=255)),
                ('fecha', models.CharField(max_length=255)),
                ('jornada', models.CharField(max_length=255)),
                ('id_local', models.CharField(max_length=255)),
                ('nombre_local', models.CharField(max_length=255)),
                ('id_visitante', models.CharField(max_length=255)),
                ('nombre_visitante', models.CharField(max_length=255)),
                ('goles_local', models.CharField(max_length=255)),
                ('goles_visitante', models.CharField(max_length=255)),
                ('id_arbitro', models.CharField(max_length=255)),
                ('nombre_arbitro', models.CharField(max_length=255)),
                ('estadio', models.CharField(max_length=255)),
            ],
        ),
    ]
