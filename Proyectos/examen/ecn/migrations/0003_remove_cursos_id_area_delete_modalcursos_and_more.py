# Generated by Django 4.1.2 on 2023-06-21 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0002_autor_categoria_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='id_Area',
        ),
        migrations.DeleteModel(
            name='ModalCursos',
        ),
        migrations.DeleteModel(
            name='AreaCursos',
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
