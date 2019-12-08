# Generated by Django 3.0 on 2019-12-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('Latitude', models.DecimalField(decimal_places=13, max_digits=15)),
                ('Longitude', models.DecimalField(decimal_places=13, max_digits=15)),
                ('Unique_squirrel_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=250)),
                ('Date', models.DateField()),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=250)),
                ('Primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=250)),
                ('Location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=250)),
                ('Specific_location', models.CharField(blank=True, max_length=250)),
                ('Running', models.BooleanField()),
                ('Chasing', models.BooleanField()),
                ('Climbing', models.BooleanField()),
                ('Eating', models.BooleanField()),
                ('Foraging', models.BooleanField()),
                ('Other_activities', models.CharField(blank=True, max_length=250)),
                ('Kuks', models.BooleanField()),
                ('Quaas', models.BooleanField()),
                ('Moans', models.BooleanField()),
                ('Tail_flags', models.BooleanField()),
                ('Tail_twitches', models.BooleanField()),
                ('Approaches', models.BooleanField()),
                ('Indifferent', models.BooleanField()),
                ('Runs_from', models.BooleanField()),
            ],
        ),
    ]
