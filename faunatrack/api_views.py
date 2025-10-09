from rest_framework import viewsets
from faunatrack.models import Espece, Scientifique
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from faunatrack.serializers import EspeceSerializer


class EspeceViewSet(viewsets.ModelViewSet):
    queryset = Espece.objects.all()
    serializer_class = EspeceSerializer




class ExampleView(APIView):
    authentication_classes = []
    permission_classes  = []
    
    def get(self, request, **kwargs):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        return Response(content)
    