# Generated by Django 5.0.4 on 2024-05-05 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('puesto', models.CharField(max_length=50, verbose_name='Puesto')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.AlterModelOptions(
            name='ingreso',
            options={'verbose_name': 'Acceso', 'verbose_name_plural': 'Accesos'},
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='ingreso',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Hora de entrada'),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ingreso.usuario', verbose_name='usuario'),
        ),
    ]