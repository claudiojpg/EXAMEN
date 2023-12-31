# Generated by Django 4.1.2 on 2023-06-15 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCursos',
            fields=[
                ('id_Area', models.AutoField(db_column='idArea', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ModalCursos',
            fields=[
                ('id_Modal', models.AutoField(db_column='idModal', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sence', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField()),
                ('modalidad', models.CharField(blank=True, max_length=30, null=True)),
                ('objetivo', models.CharField(blank=True, max_length=200, null=True)),
                ('horas', models.IntegerField()),
                ('activo', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('id_Area', models.ForeignKey(db_column='idArea', on_delete=django.db.models.deletion.CASCADE, to='ecn.areacursos')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
