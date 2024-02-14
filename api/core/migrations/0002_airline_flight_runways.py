# Generated by Django 5.0.2 on 2024-02-14 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('airline_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField()),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('aircraft_type', models.CharField(max_length=10)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.airline')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_destination', to='core.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_origin', to='core.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Runways',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runway_number', models.IntegerField()),
                ('runway_designation', models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right'), ('N', 'None')], max_length=1)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.airport')),
            ],
        ),
    ]
