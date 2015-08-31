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

                splitted_talents = talent_set.split('|')
                kw = {
                    'talent0': models.Talent.objects.get(code=splitted_talents[0])
                }
                if len(splitted_talents) > 1:
                    kw['talent1'] = models.Talent.objects.get(code=splitted_talents[1])

                ts, _ = models.TalentSet.objects.get_or_create(**kw)

                instance.talents.add(ts)


            # skills
            for skill_set in skills:

                splitted_skills = skill_set.split('|')
                kw = {
                    'skill0': models.Skill.objects.get(code=splitted_skills[0])
                }
                if len(splitted_skills) > 1:
                    kw['skill1'] = models.Skill.objects.get(code=splitted_skills[1])

                ts, _ = models.SkillSet.objects.get_or_create(**kw)

                instance.skills.add(ts)

            self.stdout.write('Loaded {0} career'.format(instance.code))

        self.stdout.write('Data loaded')
