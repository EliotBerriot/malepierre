from django.core.management.base import BaseCommand, CommandError

from malepierre import data
from malepierre.characters import models
class Command(BaseCommand):
    help = 'Load initial data in database'

    def handle(self, *args, **options):

        for row in data.careers.DATA:
            # init_fields = {field: value for field, value in row.items() if field in data.careers.INIT_FIELDS}
            # other_fields = {field: value for field, value in row.items() if field in data.careers.INIT_FIELDS}
            try:
                instance = models.Career.objects.get(code=row['code'])
            except models.Career.DoesNotExist:
                instance = models.Career()

            for field in row:
                setattr(instance, field, row[field])
            instance.save()
            self.stdout.write('Loaded {0} career'.format(instance.code))

        self.stdout.write('Data loaded')
