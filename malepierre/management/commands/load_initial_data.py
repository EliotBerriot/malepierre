from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db.models import Count
from malepierre import data
from malepierre.characters import models

class Command(BaseCommand):
    help = 'Load initial data in database'
    option_list = BaseCommand.option_list + (
        make_option('--talents',
            action='store_true',
            help='Load talents'),
        make_option('--skills',
            action='store_true',
            help='Load skills'),
        make_option('--careers',
            action='store_true',
            help='Load careers'),
        make_option('--wipe',
            action='store_true',
            help='Wipe data before importing'),
    )

    def parse_set(self, string):
        names = string.split('|')
        first_name = names[0].split(':')
        choice = 1
        prepend = []
        if len(first_name) > 1:
            choice = int(first_name[0])
            prepend.append(first_name[-1])

        return choice, prepend + [name for name in names]

    def filter_multiple_many(self, qs, iterable, attr="choices"):
        for e in iterable:
            qs = qs.filter(**{attr: e})
        return qs

    def load_set(self, element_set, model, set_model):

        max_choices, names = self.parse_set(element_set)
        kw = {'max_choices': max_choices}
        choices = model.objects.filter(code__in=names)

        if len(choices) != len(names):
            self.stdout.write('Warning: could not find all names: {0} {1}'.format(element_set, model))
        try:
            queryset = set_model.objects.annotate(choices_count=Count('choices'))
            queryset = queryset.filter(choices_count=len(choices))
            queryset = queryset.filter(max_choices=max_choices)
            queryset = self.filter_multiple_many(queryset, choices)
            ts = queryset.get()
        except set_model.DoesNotExist:

            ts = set_model(max_choices=max_choices)
            ts.save()
        ts.choices.add(*choices)

        return ts



    def handle(self, *args, **options):
        wipe = options.get('wipe', False)

        if options.get('talents'):
            self.stdout.write('Loading talents...')

            for row in data.talents.DATA:
                try:
                    instance = models.Talent.objects.get(code=row['code'])
                except models.Talent.DoesNotExist:
                    instance = models.Talent()

                declinations = row.pop('declinations', [])
                linked_skill = row.pop('linked_skill', None)

                for field in row:
                    setattr(instance, field, row[field])
                instance.save()

                for code, name in declinations:
                    d_instance, _ = models.Talent.objects.get_or_create(code=code, linked_talent=instance)
                    d_instance.name = '{0} ({1})'.format(instance.name, name)
                    d_instance.save()
                    self.stdout.write('Loaded {0} talent declination'.format(d_instance.code))

                self.stdout.write('Loaded {0} talent'.format(instance.code))


        if options.get('skills'):
            self.stdout.write('\nLoading skills...')

            for row in data.skills.DATA:
                try:
                    instance = models.Skill.objects.get(code=row['code'])
                except models.Skill.DoesNotExist:
                    instance = models.Skill()

                declinations = row.pop('declinations', [])
                linked_talents = row.pop('linked_talents', [])
                linked_skill = row.pop('linked_skill', None)

                for field in row:
                    setattr(instance, field, row[field])


                instance.save()

                talents = models.Talent.objects.filter(code__in=linked_talents)
                instance.linked_talents.add(*talents)

                for code, name in declinations:
                    d_instance, _ = models.Skill.objects.get_or_create(code=code, linked_skill=instance)
                    d_instance.name = '{0} ({1})'.format(instance.name, name)
                    d_instance.save()
                    self.stdout.write('Loaded {0} skill declination'.format(d_instance.code))

                self.stdout.write('Loaded {0} skill'.format(instance.code))

            self.stdout.write('\nloading careers...')

        if options.get('careers'):
            if wipe:
                models.Career.objects.all().delete()
                models.SkillSet.objects.all().delete()
                models.TalentSet.objects.all().delete()

            for row in data.careers.DATA:
                try:
                    instance = models.Career.objects.get(code=row['code'])
                except models.Career.DoesNotExist:
                    instance = models.Career()

                exits = models.Career.objects.filter(code__in=row.pop('exits', []))
                talents = row.pop('talents', [])
                skills = row.pop('skills', [])

                # exits

                for field in row:
                    setattr(instance, field, row[field])
                instance.save()

                instance.exits.add(*exits)

                for talent_set in talents:
                    instance.talents.add(self.load_set(talent_set, models.Talent, models.TalentSet))

                for skill_set in skills:
                    instance.skills.add(self.load_set(skill_set, models.Skill, models.SkillSet))

                self.stdout.write('Loaded {0} career'.format(instance.code))

        self.stdout.write('Data loaded')
