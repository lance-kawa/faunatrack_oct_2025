from django.contrib import admin

from faunatrack.models import Espece, Location, Observation, ObservationPhotos, Project, ProjectsMembers, Scientifique


from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EspeceResource(resources.ModelResource):

    class Meta:
        model = Espece  
        
        
class EspeceAdmin(ImportExportModelAdmin):
    list_display = ["id", "__str__", "status", ]
    list_editable = ["status"]
    
    resource_classes = [EspeceResource]
    
    
    
    
    
 
class ProjectResource(resources.ModelResource):

    class Meta:
        model = Project  
           
    
        
class ProjectMemberInline(admin.StackedInline):
    model = ProjectsMembers
    extra = 1
    fields = ['scientifique', 'roles', 'projet']
    autocomplete_fields = ['scientifique']
    
class ObservationPhotosInline(admin.TabularInline):
    model = ObservationPhotos
    extra = 1


class LocationAdmin(admin.ModelAdmin):
    pass

class ObservationAdmin(admin.ModelAdmin):
    list_display = ["espece__nom", "id"]
    inlines = [ObservationPhotosInline]
    

class ObservationPhotosAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(ImportExportModelAdmin):
    resources = [ProjectResource]
class ScientifiqueAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    inlines = [ProjectMemberInline]

admin.site.register(Espece, EspeceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Observation, ObservationAdmin)
# admin.site.register(ObservationPhotos, ObservationPhotosAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Scientifique, ScientifiqueAdmin)