from faunatrack.models import Espece
from rest_framework import serializers


class EspeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espece
        fields = "__all__"