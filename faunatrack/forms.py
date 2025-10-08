from django import forms
from django.utils import timezone

from faunatrack.models import Observation


class FaunatrackForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FaunatrackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5'
    


class ObservationForm(FaunatrackForm):
    class Meta:
        fields = "__all__"
        model = Observation
        widgets = {
            "date_observation": forms.widgets.DateInput(
                attrs={
                    "type": "date"
                }
            )
        }
        
    
    quantite = forms.IntegerField(
        label="Quantité",
        help_text="Nombre d'indidivus observés",
        min_value=1,
        max_value=1000
    )
    
    
    def clean_date_observation(self):
        date = self.cleaned_data.get("date_observation", None)
        if date and date > timezone.now():
            raise forms.ValidationError("La date ne peut pas être dans le futur")
        return date