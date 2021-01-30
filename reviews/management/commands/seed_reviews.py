import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as reviews_models
from users import models as users_models
from rooms import models as rooms_models

class Command(BaseCommand):
    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(
            reviews_models.Review,
            number,
            {
            "accuracy": lambda x: random.randint(0,5),
            "communication": lambda x: random.randint(0,5),
            "cleanliness": lambda x: random.randint(0,5),
            "location": lambda x: random.randint(0,5),
            "check_in": lambda x: random.randint(0,5),
            "value": lambda x: random.randint(0,5),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))

