# Generated by Django 2.2.9 on 2020-06-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacionados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Partnerts', verbose_name='Imagen'),
        ),
    ]