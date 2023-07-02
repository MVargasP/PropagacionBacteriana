# Generated by Django 4.2.2 on 2023-07-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BacterialStrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maturation_period', models.PositiveIntegerField()),
                ('life_expectancy', models.PositiveIntegerField()),
                ('reproduction_rate', models.PositiveIntegerField()),
            ],
        ),
    ]