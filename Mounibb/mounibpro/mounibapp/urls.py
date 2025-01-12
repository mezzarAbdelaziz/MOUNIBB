from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('about/', views.about, name='about'),  # Page à propos
    path('contact/', views.contact, name='contact'),  # Page contact
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),  # Détails d'un projet
]
