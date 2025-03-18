import json
from django.core.management.base import BaseCommand
from auctions.models import Category 

class Command(BaseCommand):
    help = "Importa categorias do arquivo JSON para o banco de dados"

    def handle(self, *args, **kwargs):
        with open("categories.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                Category.objects.get_or_create(name=item["name"])
        self.stdout.write(self.style.SUCCESS("Categorias importadas com sucesso!"))
