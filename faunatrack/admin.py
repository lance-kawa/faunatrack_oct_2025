from ast import Pass
from django.contrib import admin

from faunatrack.models import Espece, Location, Observation, ObservationPhotos, Project, Scientifique

# from faunatrack.models import Espece


# # @admin.register(Espece)
# class EspeceAdmin(admin.ModelAdmin):
#     list_display = ["nom", "nom_sic"]
#     list_filter = ["nom_sic"]
#     search_fields = ["nom", "nom_sic"]
#     ordering = ["-nom_sic"]
#     list_editable = ["nom_sic"]
    
# admin.site.register(Espece, EspeceAdmin) 

class ObservationPhotosInline(admin.TabularInline):
    model = ObservationPhotos
    extra = 1
    
    

class EspeceAdmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass

class ObservationAdmin(admin.ModelAdmin):
    inlines = [ObservationPhotosInline]
    
class ObservationPhotosAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass
class ScientifiqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Espece, EspeceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Observation, ObservationAdmin)
# admin.site.register(ObservationPhotos, ObservationPhotosAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Scientifique, ScientifiqueAdmin)