from django.core.management.base import BaseCommand
from main.scraper import save_latest_meta_data_to_db

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_latest_meta_data_to_db()