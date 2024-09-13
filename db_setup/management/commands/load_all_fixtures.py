from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Load all fixtures in one command"

    def handle(self, *args, **kwargs):
        fixtures = [
            'user_data.json',
            'custom_user_data.json',
            'pricing_data.json',
            'parking_spot_data.json',
            'ticket_data.json',
        ]

        for fixture in fixtures:
            self.stdout.write(self.style.NOTICE(f"Loading {fixture}..."))
            try:
                call_command('loaddata', fixture)
                self.stdout.write(self.style.SUCCESS(f"{fixture} loaded successfully"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to load {fixture}: {e}"))
