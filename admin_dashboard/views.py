from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from portfolio.models import Profile, Project, Skill


@login_required
def dashboard(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'projects_count': projects.count(),
        'skills_count': skills.count(),
        'recent_projects': projects[:3],
    }
    return render(request, 'admin_dashboard/dashboard.html', context)


@login_required
def profile_edit(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        if profile:
            profile.name = request.POST.get('name')
            profile.title = request.POST.get('title')
            profile.bio = request.POST.get('bio')
            profile.email = request.POST.get('email')
            profile.phone = request.POST.get('phone', '')
            profile.linkedin_url = request.POST.get('linkedin_url', '')
            profile.github_url = request.POST.get('github_url', '')
            profile.twitter_url = request.POST.get('twitter_url', '')
            
            # Handle profile image
            if request.FILES.get('profile_image'):
                profile.profile_image = request.FILES['profile_image']
            elif request.POST.get('remove_profile_image'):
                profile.profile_image.delete()
                profile.profile_image = None
            
            # Handle banner image
            if request.FILES.get('banner_image'):
                profile.banner_image = request.FILES['banner_image']
            elif request.POST.get('remove_banner_image'):
                profile.banner_image.delete()
                profile.banner_image = None
            
            # Handle resume
            if request.FILES.get('resume'):
                profile.resume = request.FILES['resume']
            elif request.POST.get('remove_resume'):
                profile.resume.delete()
                profile.resume = None
            
            profile.save()
        else:
            profile = Profile.objects.create(
                name=request.POST.get('name'),
                title=request.POST.get('title'),
                bio=request.POST.get('bio'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone', ''),
                linkedin_url=request.POST.get('linkedin_url', ''),
                github_url=request.POST.get('github_url', ''),
                twitter_url=request.POST.get('twitter_url', ''),
                profile_image=request.FILES.get('profile_image'),
                banner_image=request.FILES.get('banner_image'),
                resume=request.FILES.get('resume'),
            )
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('admin_dashboard:dashboard')
    
    context = {'profile': profile}
    return render(request, 'admin_dashboard/profile_edit.html', context)


@login_required
def projects_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'admin_dashboard/projects_list.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        project = Project.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            technologies=request.POST.get('technologies'),
            github_url=request.POST.get('github_url', ''),
            live_url=request.POST.get('live_url', ''),
            image=request.FILES.get('image'),
            order=request.POST.get('order', 0),
        )
        messages.success(request, 'Project created successfully!')
        return redirect('admin_dashboard:projects_list')
    
    return render(request, 'admin_dashboard/project_form.html')


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.technologies = request.POST.get('technologies')
        project.github_url = request.POST.get('github_url', '')
        project.live_url = request.POST.get('live_url', '')
        project.order = request.POST.get('order', 0)
        
        # Handle project image
        if request.FILES.get('image'):
            project.image = request.FILES['image']
        elif request.POST.get('remove_image'):
            project.image.delete()
            project.image = None
        
        project.save()
        messages.success(request, 'Project updated successfully!')
        return redirect('admin_dashboard:projects_list')
    
    context = {'project': project}
    return render(request, 'admin_dashboard/project_form.html', context)


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('admin_dashboard:projects_list')


@login_required
def skills_list(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'admin_dashboard/skills_list.html', context)


@login_required
def skill_create(request):
    if request.method == 'POST':
        skill = Skill.objects.create(
            name=request.POST.get('name'),
            percentage=request.POST.get('percentage'),
            category=request.POST.get('category'),
            icon=request.POST.get('icon', ''),
        )
        messages.success(request, 'Skill created successfully!')
        return redirect('admin_dashboard:skills_list')
    
    return render(request, 'admin_dashboard/skill_form.html')


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    
    if request.method == 'POST':
        skill.name = request.POST.get('name')
        skill.percentage = request.POST.get('percentage')
        skill.category = request.POST.get('category')
        skill.icon = request.POST.get('icon', '')
        skill.save()
        messages.success(request, 'Skill updated successfully!')
        return redirect('admin_dashboard:skills_list')
    
    context = {'skill': skill}
    return render(request, 'admin_dashboard/skill_form.html', context)


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('admin_dashboard:skills_list')
