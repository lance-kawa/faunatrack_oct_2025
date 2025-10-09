import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.migrations.state import ProjectState
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# La quantité et la dernière localisation des especes extinct
# Tout les scientifiques des projets public qui concernent une espece
# Afficher les 3 dernières photos prises


class BaseModel(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True



class Espece(models.Model):

    
    class Meta:
        verbose_name_plural = _("Espèces")
        verbose_name= _("Espece")
        ordering = ["nom"]
        # db_table = "faunatrack_espece"
    
    class StatusChoices(models.TextChoices):
        # CODEBASE = ( "bdd", "Human readable (interface)")
        LOW_RISK = ("lr", _("Pas en voie d'extinction"))
        HIGH_RISK = ("hr", _("En voie d'extinction"))
        EXTINCT = ("extinct", _("Y'en a plus"))
        DEFAULT = ("default", _("default"))
   
        
    nom = models.CharField(max_length=255, default="espece inconnu", unique=True)
    status = models.CharField(max_length=255, default=StatusChoices.DEFAULT, choices=StatusChoices.choices)
    
    def __str__(self):
        return f"{self.nom} - {self.status}"
    
    
class Location(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return f"Long: {self.long} Lat: {self.latitude}"


class ObservationeManager(models.Manager):
    
    def get_complex_query():
        pass
    

        
class Observation(models.Model):
    objects = ObservationeManager()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_observation = models.DateTimeField()
    espece = models.ForeignKey(Espece, on_delete=models.PROTECT, related_name="observations")
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    quantite = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)
    project = models.ForeignKey("faunatrack.Project", on_delete=models.SET_NULL, null=True, related_name="observations")
    
    def __str__(self):
        return f" {self.quantite} {self.espece.nom} at {self.location} on {self.date_observation}"


class ObservationPhotos(models.Model):
    
    class Meta:
        verbose_name_plural = _("Photos d'observations")
        verbose_name = _("Photo d'observation")
        ordering = ["observation"]
    
    photo = models.ImageField(upload_to="photos_obs/", default=None, null=True)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, related_name="photos")
    
    
    def __str__(self):
        return f"Photo: {self.photo} Observation: {self.observation}"
    
class Project(BaseModel):
    privacy = models.BooleanField(default=False)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return f"{self.titre} Private: {self.privacy}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
        
    
class ProjectsMembers(BaseModel):
    
    class RoleChoices(models.TextChoices):
        ADMIN = ("admin", "administrateur")
        MEMBER = ("member", "member")
        
    scientifique = models.ForeignKey("faunatrack.Scientifique", on_delete=models.CASCADE, related_name="project_member")  
    projet = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_member")    
    roles = models.CharField(max_length=255, choices=RoleChoices.choices, default=RoleChoices.MEMBER)
    
class Scientifique(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profil")
    projets = models.ManyToManyField(Project, through=ProjectsMembers)
    
    def __str__(self):
        return self.user.username
    
    
    
