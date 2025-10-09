from django.test import TestCase
from django.utils import timezone

from faunatrack.models import Espece, Location, Observation


# crée une base de donnée temporaire (que je peux garder pour accélérer les tests)
class TestObservation(TestCase):
    
    def setUp(self):
        # appelé à chaque test 
        # les signaux ne sont pas appelé par défaut dans les tests, il faut les conencter voir docs 
        self.observation = Observation.objects.create(
            espece=Espece.objects.create(nom="Loup"), 
            date_observation=timezone.now(), 
            location=Location.objects.create(long=50, latitude=50)
            )
        
    
        
    def tearDown(self):
        # n'oubliez pas de déco les signals dans teardow
        print("This is the end")
    
    def test_observation_has_espece(self):
        self.assertIsNotNone(self.observation.espece)

        
        
        