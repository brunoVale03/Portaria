# Generated by Django 2.2 on 2022-03-04 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0009_alter_moradores_options_alter_visitante_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moradores',
            new_name='Morador',
        ),
        migrations.AlterModelTable(
            name='morador',
            table='Morador',
        ),
    ]
