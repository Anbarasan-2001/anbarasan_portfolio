from django.shortcuts import render
from .models import Profile, Project, Skill


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/index.html', context)
