# Generated by Django 4.2 on 2023-04-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_domicio_paciente_domicilio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='apellido_materno',
            field=models.CharField(default='No ingresado', max_length=60),
        ),
        migrations.AddField(
            model_name='paciente',
            name='apellido_paterno',
            field=models.CharField(default='No ingresado', max_length=60),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
