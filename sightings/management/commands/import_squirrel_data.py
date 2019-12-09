import csv
import re
from django.core.management.base import BaseCommand
from sightings.models import Squirrel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('SquirrelData')
    def handle(self, *args, **options):
        with open(options['SquirrelData'],'r') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            for row in data:

                def StrChange(str_):
                    if str.lower(str_)=='true':
                        return True
                    else:
                        return False

                if re.search(r'(\d{2})(\d{2})(\d{4})',row['Date']):
                    BoolMatch = re.search(r'(\d{2})(\d{2})(\d{4})',row['Date'])

                p = Squirrel(
                            Latitude=row['Y'],
                            Longitude=row['X'],
                            Unique_squirrel_id=row['Unique Squirrel ID'],
                            Shift=row['Shift'],
                            Date='-'.join([BoolMatch.group(3),BoolMatch.group(1),BoolMatch.group(2)]),
                            Age=row['Age'],
                            Primary_fur_color=row['Primary Fur Color'],
                            Location=row['Location'],
                            Specific_location=row['Specific Location'],
                            Running=StrChange(row['Running']),
                            Chasing=StrChange(row['Chasing']),
                            Climbing=StrChange(row['Climbing']),
                            Eating=StrChange(row['Eating']),
                            Foraging=StrChange(row['Foraging']),
                            Other_activities=row['Other Activities'],
                            Kuks=StrChange(row['Kuks']),
                            Quaas=StrChange(row['Quaas']),
                            Moans=StrChange(row['Moans']),
                            Tail_flags=StrChange(row['Tail flags']),
                            Tail_twitches=StrChange(row['Tail twitches']),
                            Approaches=StrChange(row['Approaches']),
                            Indifferent=StrChange(row['Indifferent']),
                            Runs_from=StrChange(row['Runs from'])
                )

                p.save()