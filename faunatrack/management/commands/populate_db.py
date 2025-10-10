from django.core.management.base import BaseCommand

from faunatrack.models import Espece

import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Commande pour générer des données en base'
    
    def add_arguments(self, parser):
        parser.add_argument("--siberie", type=str, help="Créer seulement des espèces de sibérie")
    
    
    def handle(self, *args, **kwargs):
        siberie = kwargs.get('siberie', None)
        
        if siberie == "oui":
            name = "Ours de sibérie"
            Espece.objects.create(nom=name)
        else:
            name = "Ours brun"
            Espece.objects.create(nom=name)
        logger.info(name)
        from faunatrack.tasks.add import add
        
        add.apply_async()

 