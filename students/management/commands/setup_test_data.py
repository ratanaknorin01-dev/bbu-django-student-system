
from django.core.management.base import BaseCommand, CommandError
from scripts.generate_khmer_data import run_seed


class Command(BaseCommand):
    help = "Generate test data for students"

    def add_arguments(self, parser):
        parser.add_argument(
            "--student-count",
            type=int,
            default=100,
        )

    def handle(self, *args, **options):
        count = options["student_count"]

        if count < 0:
            raise CommandError("Student count cannot be negative.")

        run_seed(count)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully generated {count} students!"
            )
        )
