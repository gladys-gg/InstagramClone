from django.urls import path
from . import views

#apps urls
urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login_request, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('settings', views.profile, name = 'profile'),
]

