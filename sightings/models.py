from django.db import models


class Squirrel(models.Model):
    Latitude = models.DecimalField(max_digits=15, decimal_places=13)
    Longitude = models.DecimalField(max_digits=15, decimal_places=13)

    Unique_squirrel_id = models.CharField(primary_key=True, max_length=250)

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'),)
    Shift = models.CharField(max_length=250, choices=SHIFT_CHOICES, )

    Date = models.DateField()

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = ((ADULT, 'Adult'), (JUVENILE, 'Juvenile'),)
    Age = models.CharField(max_length=250, choices=AGE_CHOICES, )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    FUR_CHOICES = ((GRAY, 'Gray'), (CINNAMON, 'Cinnamon'), (BLACK, 'Black'),)
    Primary_fur_color = models.CharField(max_length=250, choices=FUR_CHOICES, )

    GROUNDPLANE = 'Ground Plane'
    ABOVEGROUND = 'Above Ground'
    LOCATION_CHOICES = ((GROUNDPLANE, 'Ground Plane'), (ABOVEGROUND, 'Above Ground'),)
    Location = models.CharField(max_length=250, choices=LOCATION_CHOICES, )

    Specific_location = models.CharField(max_length=250, blank=True)

    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()

    Other_activities = models.CharField(max_length=250, blank=True)

    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()

