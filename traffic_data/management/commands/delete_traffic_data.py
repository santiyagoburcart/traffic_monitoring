from django.core.management.base import BaseCommand
from traffic_data.models import TrafficData

class Command(BaseCommand):
    help = 'Delete all traffic data records'

    def handle(self, *args, **options):
        TrafficData.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All traffic data records have been deleted successfully.'))
