# Generated by Django 2.2.9 on 2020-01-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order', 'title'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
