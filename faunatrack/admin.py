from django.contrib import admin

from faunatrack.models import Espece, Location, Observation, ObservationPhotos, Project, ProjectsMembers, Scientifique


class ProjectMemberInline(admin.StackedInline):
    model = ProjectsMembers
    extra = 1
    fields = ['scientifique', 'roles', 'projet']
    autocomplete_fields = ['scientifique']
    
class ObservationPhotosInline(admin.TabularInline):
    model = ObservationPhotos
    extra = 1

class EspeceAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "status", ]
    list_editable = ["status"]

class LocationAdmin(admin.ModelAdmin):
    pass

class ObservationAdmin(admin.ModelAdmin):
    list_display = ["espece__nom"]
    inlines = [ObservationPhotosInline]
    

class ObservationPhotosAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass
class ScientifiqueAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    inlines = [ProjectMemberInline]

admin.site.register(Espece, EspeceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Observation, ObservationAdmin)
# admin.site.register(ObservationPhotos, ObservationPhotosAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Scientifique, ScientifiqueAdmin)