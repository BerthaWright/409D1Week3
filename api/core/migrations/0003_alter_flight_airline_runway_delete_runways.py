# Generated by Django 5.0.2 on 2024-02-14 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_airline_flight_runways'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='airline', to='core.airline'),
        ),
        migrations.CreateModel(
            name='Runway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runway_number', models.IntegerField()),
                ('runway_designation', models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right'), ('N', 'None')], max_length=1)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runways', to='core.airport')),
            ],
        ),
        migrations.DeleteModel(
            name='Runways',
        ),
    ]