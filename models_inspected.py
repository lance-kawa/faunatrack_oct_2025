
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class FaunatrackEspece(models.Model):
    status = models.CharField(max_length=255)
    nom = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'faunatrack_espece'


class FaunatrackLocation(models.Model):
    long = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    latitude = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'faunatrack_location'


class FaunatrackObservation(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_observation = models.DateTimeField()
    quantite = models.IntegerField()
    espece = models.ForeignKey(FaunatrackEspece, models.DO_NOTHING)
    location = models.ForeignKey(FaunatrackLocation, models.DO_NOTHING)
    project = models.ForeignKey('FaunatrackProject', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faunatrack_observation'


class FaunatrackObservationphotos(models.Model):
    photo = models.CharField(max_length=100, blank=True, null=True)
    observation = models.ForeignKey(FaunatrackObservation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faunatrack_observationphotos'


class FaunatrackProject(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    privacy = models.BooleanField()
    titre = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'faunatrack_project'


class FaunatrackProjectsmembers(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    roles = models.CharField(max_length=255)
    projet = models.ForeignKey(FaunatrackProject, models.DO_NOTHING)
    scientifique = models.ForeignKey('FaunatrackScientifique', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faunatrack_projectsmembers'


class FaunatrackScientifique(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faunatrack_scientifique'
