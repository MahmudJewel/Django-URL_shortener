from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
import pytz

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

        # disable urls for expired date 
        for url in urls:
            expire_time = url.created_at + timedelta(url.expiration_day)
            # now = datetime.utcnow()
            now = datetime.now()
            now = pytz.utc.localize(now)
            if expire_time<=now:
                url.is_deleted=True
                # url.save()
                print(now,' ==> ', expire_time, 'id= ', url.id)

        self.stdout.write(self.style.SUCCESS('Successfully closed expired url '))
