from django.core.management.base import BaseCommand
from main.scraper import create_mlbb_meta_data

class Command(BaseCommand):
    def handle(self, *args, **options):
        create_mlbb_meta_data()