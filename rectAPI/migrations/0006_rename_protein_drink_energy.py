# Generated by Django 3.2 on 2021-11-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rectAPI', '0005_drink_hamburger_pizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='protein',
            new_name='energy',
        ),
    ]
