# Generated by Django 3.2 on 2021-05-04 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.FloatField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(max_length=255)),
                ('characteristic_set', models.ManyToManyField(to='pets.Characteristic')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.group')),
            ],
        ),
    ]
