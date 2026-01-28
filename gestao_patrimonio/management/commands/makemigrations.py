from django.core.management.commands.makemigrations import Command as MakeMigrations


class Command(MakeMigrations):
    def handle(self, *args, **options):
        options['empty'] = False
        options['dry_run'] = False
        super().handle(*args, **options)
