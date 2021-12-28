from django.db.models.expressions import F
from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns=[
    path('',  views.apiOverview, name='api-overview'),
    path('get-all-animals/',  views.getAnimals, name='get-all-animals'),
    path('single-animal/<str:id>',  views.getSingleAnimal, name='get-single-animal'),
    path('create-animal',  views.createAnimal, name='create-animal'),
    path('update-animal/<str:id>',  views.updateAnimal, name='update-animal'),
    path('delete-animal/<str:id>',  views.deleteAnimal, name='delete-animal'),
]