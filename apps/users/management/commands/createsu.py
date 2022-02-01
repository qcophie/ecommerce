from django.core.management.base import BaseCommand
from apps.users.models import SEUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not SEUser.objects.filter(email="africasoko@gmail.com").exists():
            SEUser.objects.create_superuser("africasoko@gmail.com", "@New0246882769", "@New0246882769", '@New0246882769')
