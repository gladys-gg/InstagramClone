from django.urls import path
from . import views

#apps urls
urlpatterns = [
    path('', views.index, name = 'index')
]

