from faunatrack.models import Espece, Observation, Location, Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class EspeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espece
        fields = "__all__"
        
        
class ObservationSerializer(serializers.ModelSerializer):
    
    espece = EspeceSerializer()
    location = LocationSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Observation
        fields = "__all__"
        
    def to_representation(self, instance):
        if instance.project and instance.project.privacy:
            self.fields.pop('espece', None)
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    
    def update(self, instance, validated_data):
        espece_json = validated_data.get("espece", instance.espece)
        espece = Espece.objects.create(**espece_json)
        instance.espece = espece
        instance.save()
        return instance
    
    def validate_status(self, value):
        if not Espece.StatusChoices.choices.contains(value):
            raise serializers.ValidationError("Statut non valide")
        return value