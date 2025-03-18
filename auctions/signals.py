from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

@receiver(post_migrate)
def run_importar_categorias(sender, **kwargs):
    from django.apps import apps
    if apps.is_installed("auctions"):
        call_command("importar_categorias")
