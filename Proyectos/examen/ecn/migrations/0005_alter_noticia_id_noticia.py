# Generated by Django 4.1.2 on 2023-06-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0004_remove_noticia_id_remove_noticia_url_amigable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='id_noticia',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
