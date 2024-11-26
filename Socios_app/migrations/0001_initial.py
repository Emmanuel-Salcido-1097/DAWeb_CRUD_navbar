# Generated by Django 5.1.2 on 2024-11-22 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('Id_Socio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_socio', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('aporte', models.CharField(max_length=100)),
                ('beneficio', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
                'db_table': 'Socios',
            },
        ),
    ]