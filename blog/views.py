from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import BlogPost
from app.forms import ContactForm
from app.models import ContactMessage

def home(request):
    # Import app models
    from app.models import Skill, Project, Achievement, Experience
    
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save(commit=False)
            contact_message.ip_address = get_client_ip(request)
            contact_message.user_agent = request.META.get('HTTP_USER_AGENT', '')
            contact_message.save()
            
            # Send email notification
            try:
                send_contact_email(contact_message)
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            except Exception as e:
                messages.warning(request, 'Your message was saved, but there was an issue sending the email notification.')
            
            # Redirect to prevent form resubmission
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/#contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    # Get featured content for the home page
    skills = Skill.objects.filter(is_featured=True)
    projects = Project.objects.filter(is_featured=True)
    achievements = Achievement.objects.filter(is_featured=True)[:3]
    experiences = Experience.objects.filter(is_featured=True)[:2]
    
    # Get recent blog posts
    try:
        recent_posts = BlogPost.objects.order_by('-created_on')[:3]
    except:
        recent_posts = []
    
    context = {
        'skills': skills,
        'projects': projects,
        'achievements': achievements,
        'experiences': experiences,
        'recent_posts': recent_posts,
        'contact_form': form,
    }
    
    return render(request, 'index.html', context)

def get_client_ip(request):
    """Get the client IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_contact_email(contact_message):
    """Send email notification when a contact form is submitted"""
    subject = f'New Contact Form Submission: {contact_message.subject}'
    
    message_body = f"""
    New contact form submission from your portfolio:

    Name: {contact_message.name}
    Email: {contact_message.email}
    Phone: {contact_message.phone or 'Not provided'}
    Company: {contact_message.company or 'Not provided'}
    Subject: {contact_message.subject}

    Message:
    {contact_message.message}

    Submitted at: {contact_message.created_at}
    IP Address: {contact_message.ip_address}
    """
    
    # Send email to you
    send_mail(
        subject=subject,
        message=message_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL],
        fail_silently=False,
    )
    
    # Send confirmation email to the sender
    confirmation_subject = f'Thank you for contacting Mahendra Dhakal'
    confirmation_message = f"""
    Hello {contact_message.name},

    Thank you for reaching out! I've received your message about "{contact_message.subject}" and will get back to you as soon as possible.

    Your message:
    {contact_message.message}

    Best regards,
    Mahendra Dhakal
    Civil Engineer & Developer
    mahendradhakal700@gmail.com
    +977-9806714549
    """
    
    send_mail(
        subject=confirmation_subject,
        message=confirmation_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[contact_message.email],
        fail_silently=True,  # Don't fail if confirmation email fails
    )

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_on')
    return render(request, 'list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'details.html', {'post': post})