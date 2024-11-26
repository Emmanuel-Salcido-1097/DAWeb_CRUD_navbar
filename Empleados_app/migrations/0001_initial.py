# Generated by Django 5.1.2 on 2024-11-22 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('Id_Empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('celular', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleados',
            },
        ),
    ]
