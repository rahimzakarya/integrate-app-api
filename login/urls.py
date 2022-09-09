from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.get_users),
    path('users/add', views.addUser ),

    path('resources/<str:speciality>/<str:level>', views.get_resources),
    path('resources/add', views.addResources),
]