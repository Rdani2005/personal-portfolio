from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.HomeView.as_view(), name='projects_home'),
    path('projects/', views.ProjectsView.as_view(), name='projects_list'),

]
