from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy

from faunatrack.forms import ObservationForm
from faunatrack.models import Espece, Observation, ObservationPhotos, Scientifique
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
        last_obs: Observation = specie.observations.order_by("date_observation").last()
        obs_extincts.append(last_obs)
        
    # obs_test = Observation.objects.filter(espece__status=Espece.StatusChoices.EXTINCT)
        
    obs_ids = Observation.objects.filter(espece__nom="Loup").values_list("id", flat=True)
    
    scientifiques = Scientifique.objects.all()
    
    photos = ObservationPhotos.objects.all()[:3]
    
    from django.template.loader import render_to_string

    # Prepare context for the email template
    email_context = {
        "title": "Faunatrack October 2025",
        "last_extincts": obs_extincts,
        "photos": photos,
        "scientifiques": scientifiques,
    }

    # Render the HTML content using the home.html template
    html_message = render_to_string("home.html", email_context)

    # Send the email to all scientifiques' email addresses
    recipient_list = [s.user.email for s in scientifiques if s.user.email]

    # if recipient_list:
    #     send_mail(
    #         subject="Résumé des observations",
    #         message="Bonjour, veuillez trouver le résumé des observations ci-dessous.",
    #         from_email="admin@monappdjango.com",
    #         recipient_list=recipient_list,
    #         html_message=html_message,
    #     )


    return render(request, "home.html", context={
        "title": "Faunatrack October 2025",
        "last_extincts": obs_extincts,  # QS are lazy evaluated so the actual db call is done only when needed
        "photos": photos,  # QS are lazy evaluated so the actual db call is done only when needed
        "scientifiques": scientifiques,  # QS are lazy evaluated so the actual db call is done only when needed
        # "obs_test": obs_test
        
    })
    
    


class ObservationList(ListView):
    model = Observation
    queryset = Observation.objects.all()
    template_name = "observations/list.html"   
    
    
class ObservationCreate(CreateView):
    model = Observation
    template_name= "observations/create_update.html"
    form_class = ObservationForm
    success_url = reverse_lazy("home")
    extra_context = {"action": "Ajouter"}
    

class ObservationUpdate(UpdateView):
    model = Observation
    template_name = "observations/create_update.html"
    form_class = ObservationForm
    success_url = reverse_lazy("observation_list")
    extra_context = {"action": "Modifier"}
    
            
    def post(self, request, *args, **kwargs):
        print("Bonjour")
        return super().post(request, *args, **kwargs)
    

class ObservationDetail(DetailView):
    model = Observation
    template_name = "observations/detail.html"


class ObservationDelete(DeleteView):
    model = Observation
    template_name = "observations/delete.html"
    success_url = reverse_lazy("observation_list")
