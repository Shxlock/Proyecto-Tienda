# Generated by Django 4.2 on 2023-12-26 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='uptaded',
            new_name='updated',
        ),
    ]
