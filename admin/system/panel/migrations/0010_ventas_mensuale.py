# Generated by Django 4.1.7 on 2024-07-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas_Mensuale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
