# Generated by Django 4.1.1 on 2022-09-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Mi Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AddField(
            model_name='libro',
            name='visitas',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]