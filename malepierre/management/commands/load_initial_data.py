from django.core.management.base import BaseCommand, CommandError

from malepierre import data
from malepierre.characters import models
class Command(BaseCommand):
    help = 'Load initial data in database'

    def handle(self, *args, **options):

        self.stdout.write('Loading talents...')

        for row in data.talents.DATA:
            try:
                instance = models.Talent.objects.get(code=row['code'])
            except models.Talent.DoesNotExist:
                instance = models.Talent()

            for field in row:
                setattr(instance, field, row[field])
            instance.save()

            self.stdout.write('Loaded {0} talent'.format(instance.code))

        self.stdout.write('Loading careers...')

        for row in data.careers.DATA:
            try:
                instance = models.Career.objects.get(code=row['code'])
            except models.Career.DoesNotExist:
                instance = models.Career()

            exits = models.Career.objects.filter(code__in=row.pop('exits', []))
            for field in row:
                setattr(instance, field, row[field])
            instance.save()

            instance.exits.add(*exits)

            self.stdout.write('Loaded {0} career'.format(instance.code))

        self.stdout.write('Data loaded')
