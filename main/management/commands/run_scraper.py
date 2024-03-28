from django.core.management.base import BaseCommand
from main.scraper import scrape_mlbb_meta_data

class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_mlbb_meta_data()