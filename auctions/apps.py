from django.apps import AppConfig
import os

class AuctionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auctions"

    def ready(self):
        if os.environ.get("RUN_MAIN", None) == "true": 
            from django.core.management import call_command
            call_command("importar_categorias")

