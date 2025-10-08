from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone

from faunatrack.forms import ObservationForm
from faunatrack.models import Espece, Observation, ObservationPhotos, Scientifique
from django.db.models import OuterRef, Subquery
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
def home(request: HttpRequest):
    user = request.user 
    
    # worlf =Espece.objects.all().filter(nom="Loup").first()
    # extinct_species  = Espece.objects.order_by("nom").last()
    # try:
    #     # extinct_species  = Espece.objects.get(pk=3)
        # extinct_species  = Espece.objects.all()
        # extinct_species  = extinct_species.filter(nom="Loup")
    # except Espece.DoesNotExist:
    #     pass
    # extinct_species = Observation.objects.filter(date_observation__lte=timezone.now() - timezone.timedelta(hours=10))
    # extinct_species = Observation.objects.exclude(date_observation__lte=timezone.now() - timezone.timedelta(hours=10))
    # extinct_species = Observation.objects.filter(espece__nom="Ours Polaire").filter(date_observation__lte=timezone.now())
    
    # loup, created = Espece.objects.get_or_create(nom="Loup", defaults={"status": "lr"})
    # loup = Espece.objects.create(nom="Loup")
    
    # defaults = Espece.objects.filter(status=Espece.StatusChoices.DEFAULT)
    
    # for espece in defaults:
    #     espece.status = Espece.StatusChoices.LOW_RISK
    #     espece.save()
    
    # especes = Espece.objects.filter(nom__startswith="L")
    
    # especes.update(status=Espece.StatusChoices.HIGH_RISK)
    # obs_ordered = Observation.objects.all()
    especes = Espece.objects.filter(status=Espece.StatusChoices.EXTINCT).prefetch_related("observations")
    obs_extincts = []
    for specie in especes:
        last_obs = specie.observations.order_by("date_observation").last()
        obs_extincts.append(last_obs)
        
    # obs_test = Observation.objects.filter(espece__status=Espece.StatusChoices.EXTINCT)
        
    obs_ids = Observation.objects.filter(espece__nom="Loup").values_list("id", flat=True)
    
    scientifiques = Scientifique.objects.filter(projets__privacy=False, projets__observations__in=obs_ids)
    
    photos = ObservationPhotos.objects.all()[:3]


    return render(request, "home.html", context={
        "title": "Faunatrack October 2025",
        "last_extincts": obs_extincts,  # QS are lazy evaluated so the actual db call is done only when needed
        "photos": photos,  # QS are lazy evaluated so the actual db call is done only when needed
        "scientifiques": scientifiques,  # QS are lazy evaluated so the actual db call is done only when needed
        # "obs_test": obs_test
        
    })
    
    


class ObservationList(ListView):
    model = Observation
    queryset = Observation.objects.filter(espece__nom="Loup")
    template_name = "observations/list.html"   
    
    
class ObservationCreate(CreateView):
    model = Observation
    template_name= "observations/create.html"
    form_class = ObservationForm
    success_url = reverse_lazy("observation_list")