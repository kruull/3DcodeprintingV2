# Generated by Django 2.2.9 on 2020-05-30 14:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Description',
            field=ckeditor.fields.RichTextField(verbose_name='Descipción'),
        ),
    ]