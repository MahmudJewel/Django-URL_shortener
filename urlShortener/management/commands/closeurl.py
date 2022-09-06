from django.core.management.base import BaseCommand, CommandError

from urlShortener.models import ShortURLS


class Command(BaseCommand):
    help = 'Disabling URL for expired date'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            urls = ShortURLS.objects.filter(is_deleted=False)
        except ShortURLS.DoesNotExist:
            raise CommandError('Url does not exist')
        for url in urls:
            print(url)

        self.stdout.write(self.style.SUCCESS('Successfully closed poll '))
