from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

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
    )

    def parse_set(self, string):
        names = string.split('|')
        first_name = names[0].split(':')
        choice = 1
        if len(first_name) > 1:
            first_name = first_name[-1]
            choice = int(first_name[0])
        return choice, [name for name in names]

    def handle(self, *args, **options):
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

                # talents
                for talent_set in talents:
                    max_choices, names = self.parse_set(talent_set)
                    kw = {'max_choices': max_choices}
                    choices = []
                    try:
                        for name in names:
                            try:
                                choices.append(models.Talent.objects.get(code=name))
                            except IndexError:
                                pass
                    except models.Talent.DoesNotExist:
                        self.stdout.write('Warning: cannot find {0} talent'.format(talent_set))
                    try:
                        ts = models.TalentSet.objects.get(max_choices=max_choices, choices__id=choices[0].pk)
                    except models.TalentSet.DoesNotExist:
                        ts = models.TalentSet(max_choices=max_choices)
                        ts.save()
                    ts.choices.add(*choices)

                    instance.talents.add(ts)


                # talents
                for skill_set in skills:
                    max_choices, names = self.parse_set(skill_set)
                    kw = {'max_choices': max_choices}
                    choices = []
                    try:
                        for name in names:
                            try:
                                choices.append(models.Skill.objects.get(code=name))
                            except IndexError:
                                pass
                    except models.Talent.DoesNotExist:
                        self.stdout.write('Warning: cannot find {0} skill'.format(skill_set))
                    try:
                        ts = models.SkillSet.objects.get(max_choices=max_choices, choices__id=choices[0].pk)
                    except models.SkillSet.DoesNotExist:
                        ts = models.SkillSet(max_choices=max_choices)
                        ts.save()
                    ts.choices.add(*choices)

                    instance.skills.add(ts)


                self.stdout.write('Loaded {0} career'.format(instance.code))

        self.stdout.write('Data loaded')
