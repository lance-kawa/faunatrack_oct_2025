from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from faunatrack.models import Espece, Observation, Scientifique
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from faunatrack.serializers import EspeceSerializer, ObservationSerializer


class EspeceViewSet(viewsets.ModelViewSet):
    permission_classes = []
    lookup_field = "nom"

    queryset = Espece.objects.all().order_by('id')
    serializer_class = EspeceSerializer

class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

    def get_queryset(self):
        return Observation.objects.all().order_by('id')
    
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ObservationSerializer
        # return ObservationDetailSerializer



class ExampleView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwargs):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        return Response(content)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)