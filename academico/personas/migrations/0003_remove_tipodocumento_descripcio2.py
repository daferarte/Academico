# Generated by Django 4.1 on 2022-08-13 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_tipodocumento_descripcio2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipodocumento',
            name='descripcio2',
        ),
    ]