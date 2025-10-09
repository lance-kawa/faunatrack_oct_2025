from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver

from faunatrack.models import Scientifique


@receiver(post_save, sender=get_user_model())
def add_scientifique_when_user_created(sender, instance, created, **kwargs):
    # sender = User (le modèle)
    # instance => l'utilisateru qui a été créé ou updaté.
    if created:
        Scientifique.objects.create(user=instance)
    