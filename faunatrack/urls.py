"""
URL configuration for pythagore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from faunatrack.views import ObservationCreate, ObservationDelete, ObservationDetail, ObservationList, ObservationUpdate, home

urlpatterns = [
    path('obs/', ObservationList.as_view(), name="observation_list"),
    path('obs/add/', ObservationCreate.as_view(), name="observation_create"),
    path('obs/update/<int:pk>/', ObservationUpdate.as_view(), name="observation_update"),
    path('obs/<int:pk>/', ObservationDetail.as_view(), name="observation_detail"),
    path('obs/delete/<int:pk>/', ObservationDelete.as_view(), name="observation_delete"),
    # path('auth/', include('django.contrib.auth.urls'))
]  


