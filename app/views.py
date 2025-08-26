from django.shortcuts import render
from .models import Skill, Project, Achievement, Experience

def home(request):
    # Get featured content for the home page
    skills = Skill.objects.filter(is_featured=True)
    projects = Project.objects.filter(is_featured=True)
    achievements = Achievement.objects.filter(is_featured=True)[:3]  # Show top 3
    experiences = Experience.objects.filter(is_featured=True)[:2]  # Show recent 2
    
    # Get recent blog posts (from blog app)
    from blog.models import Post
    recent_posts = Post.objects.all()[:3]
    
    context = {
        'skills': skills,
        'projects': projects,
        'achievements': achievements,
        'experiences': experiences,
        'recent_posts': recent_posts,
    }
    
    return render(request, 'index.html', context)

def skills_detail(request):
    """Detailed skills page showing all skills organized by category"""
    skills_by_category = {}
    categories = Skill.CATEGORY_CHOICES
    
    for category_key, category_name in categories:
        skills = Skill.objects.filter(category=category_key)
        if skills.exists():
            skills_by_category[category_name] = skills
    
    context = {
        'skills_by_category': skills_by_category,
    }
    
    return render(request, 'skills_detail.html', context)

def projects_detail(request):
    """Detailed projects page showing all projects"""
    projects = Project.objects.all()
    
    # Group projects by status if needed
    completed_projects = projects.filter(status='completed')
    in_progress_projects = projects.filter(status='in_progress')
    
    context = {
        'projects': projects,
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects,
    }
    
    return render(request, 'projects_detail.html', context)

def about_detail(request):
    """Detailed about page with achievements and experience"""
    achievements = Achievement.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'achievements': achievements,
        'experiences': experiences,
    }
    
    return render(request, 'about_detail.html', context)