# Generated by Django 2.2.9 on 2020-05-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Material')),
                ('Description', models.TextField(verbose_name='Descipción')),
                ('image', models.ImageField(upload_to='materials', verbose_name='Imagen')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiales',
                'ordering': ['order', 'title'],
            },
        ),
    ]
