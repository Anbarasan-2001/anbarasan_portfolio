from django.shortcuts import render
from .models import Profile, Project, Skill


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('category', 'name')
    
    # Process technologies for each project
    for project in projects:
        if project.technologies:
            project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/index.html', context)
