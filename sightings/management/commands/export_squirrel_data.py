import csv
from sightings.models import Squirrel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('SquirrelData.csv')
    def handle(self, *args, **options):
        fields_list = [x.name for x in Squirrel._meta.fields]
        with open(options['SquirrelData.csv'],'w') as fp:
            writer = csv.writer(fp)
            row = [ 'Latitude',
                    'Longitude',
                    'Unique_squirrel_id',
                    'Shift',
                    'Date',
                    'Age',
                    'Primary_fur_color',
                    'Location',
                    'Specific_location',
                    'Running','Chasing',
                    'Climbing',
                    'Eating',
                    'Foraging',
                    'Other_activities',
                    'Kuks',
                    'Quaas',
                    'Moans',
                    'Tail_flags',
                    'Tail_twitches',
                    'Approaches',
                    'Indifferent',
                    'Runs_from',
                    ]
            writer.writerow(row)
            for row in Squirrel.objects.all():
                row1 = [getattr(row, field) for field in fields_list]
                writer.writerow(row1)
