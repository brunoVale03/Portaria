# Generated by Django 3.2.7 on 2022-03-08 15:06

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0011_auto_20220308_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morador',
            name='CPF',
            field=cpf_field.models.CPFField(max_length=14, primary_key=True, serialize=False, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='CPF',
            field=cpf_field.models.CPFField(max_length=14, primary_key=True, serialize=False, verbose_name='CPF'),
        ),
    ]
