# Generated by Django 5.0.6 on 2024-07-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tienda', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('f_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('realizado', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Tareas Diarias',
            },
        ),
    ]
