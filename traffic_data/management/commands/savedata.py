from django.core.management.base import BaseCommand
from traffic_data.save_traffic import start_traffic_sniffing

class savedata(BaseCommand):
    help = 'Starts sniffing traffic and saves data to the database'

    def handle(self, *args, **options):
        start_traffic_sniffing()
