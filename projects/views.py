from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import Project
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'projects/home.html')


class ProjectsView(View):
    def get(self, request):
        projects = Project.projects.all()
        return render(request, 'projects/projects.html', {'projects': projects})