# Generated by Django 4.2.7 on 2023-11-24 12:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StarWarsPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=5)),
                ('mass', models.CharField(max_length=5)),
                ('hair_color', models.CharField(max_length=50)),
                ('skin_color', models.CharField(max_length=50)),
                ('eye_color', models.CharField(max_length=50)),
                ('birth_year', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('homeworld', models.URLField()),
                ('created', models.DateTimeField()),
                ('edited', models.DateTimeField()),
                ('url', models.URLField()),
                ('films', models.ManyToManyField(blank=True, to='swapi.film', verbose_name='list of films')),
                ('species', models.ManyToManyField(blank=True, to='swapi.species', verbose_name='list of species')),
                ('starships', models.ManyToManyField(blank=True, to='swapi.starship', verbose_name='list of starships')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swapi.starwarspeople')),
            ],
        ),
        migrations.AddField(
            model_name='starwarspeople',
            name='vehicles',
            field=models.ManyToManyField(blank=True, to='swapi.vehicle', verbose_name='list of vehicles'),
        ),
    ]
