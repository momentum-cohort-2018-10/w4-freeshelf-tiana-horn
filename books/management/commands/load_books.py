from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from books.models import Book
from django.core.files import File

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)

class Command(BaseCommand):
    help = "Load dogs from initial_data/books.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(get_path('books.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    name=row['name'],
                    description=row['description'],
                )
            book.save()
        print(f"{i} books loaded!")