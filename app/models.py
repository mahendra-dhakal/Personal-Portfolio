from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('devops', 'DevOps & Cloud'),
        ('tools', 'Tools & Technologies'),
        ('ai_ml', 'AI & Machine Learning'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency level from 0 to 100"
    )
    description = models.TextField(max_length=500, help_text="Brief description of your experience with this skill")
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji or icon class")
    is_featured = models.BooleanField(default=True, help_text="Show this skill on the main page")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, help_text="Brief description for cards")
    
    # URLs and Links
    demo_url = models.URLField(blank=True, help_text="Live demo URL")
    github_url = models.URLField(blank=True, help_text="GitHub repository URL")
    case_study_url = models.URLField(blank=True, help_text="Detailed case study URL")
    
    # Visual Assets
    image = models.ImageField(upload_to='projects/', blank=True, help_text="Project screenshot or logo")
    video_url = models.URLField(blank=True, help_text="Demo video URL (YouTube, Vimeo, etc.)")
    
    # Project Details
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    technologies = models.ManyToManyField(Skill, blank=True, help_text="Technologies used in this project")
    tech_tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tech tags (fallback if not using Skill model)")
    
    # Features and Highlights
    key_features = models.TextField(blank=True, help_text="Key features, one per line")
    challenges = models.TextField(blank=True, help_text="Technical challenges overcome")
    learnings = models.TextField(blank=True, help_text="What you learned from this project")
    
    # Meta Information
    is_featured = models.BooleanField(default=True, help_text="Show this project on the main page")
    is_personal = models.BooleanField(default=True, help_text="Personal project vs client work")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers first)")
    
    # Timestamps
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tech_list(self):
        """Get list of technologies, prioritizing ManyToMany relationship"""
        if self.technologies.exists():
            return [skill.name for skill in self.technologies.all()]
        elif self.tech_tags:
            return [tag.strip() for tag in self.tech_tags.split(',')]
        return []
    
    def get_features_list(self):
        """Convert key_features text to list"""
        if self.key_features:
            return [feature.strip() for feature in self.key_features.split('\n') if feature.strip()]
        return []

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('certification', 'Certification'),
        ('award', 'Award'),
        ('recognition', 'Recognition'),
        ('publication', 'Publication'),
        ('speaking', 'Speaking Engagement'),
        ('contribution', 'Open Source Contribution'),
        ('education', 'Education'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    organization = models.CharField(max_length=200, help_text="Issuing organization or institution")
    description = models.TextField(blank=True)
    date_achieved = models.DateField()
    
    # Links and Verification
    certificate_url = models.URLField(blank=True, help_text="Link to certificate or verification")
    credential_id = models.CharField(max_length=100, blank=True, help_text="Certificate or credential ID")
    
    # Display Options
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji or icon class")
    is_featured = models.BooleanField(default=True, help_text="Show on main page")
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-date_achieved']
    
    def __str__(self):
        return f"{self.title} - {self.organization}"

class Experience(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('volunteer', 'Volunteer'),
    ]
    
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current position")
    
    # Links
    company_url = models.URLField(blank=True)
    
    # Skills and Technologies
    technologies_used = models.ManyToManyField(Skill, blank=True)
    
    # Display
    company_logo = models.ImageField(upload_to='companies/', blank=True)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    @property
    def is_current(self):
        return self.end_date is None

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, help_text="Full name of the person")
    email = models.EmailField(help_text="Email address for response")
    subject = models.CharField(max_length=300, help_text="Subject of the message")
    message = models.TextField(help_text="The actual message content")
    
    # Additional info
    phone = models.CharField(max_length=20, blank=True, help_text="Optional phone number")
    company = models.CharField(max_length=200, blank=True, help_text="Optional company name")
    
    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark as read")
    is_replied = models.BooleanField(default=False, help_text="Mark as replied")
    
    # IP and user agent for security
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"
    
    def mark_as_read(self):
        self.is_read = True
        self.save()
    
    def mark_as_replied(self):
        self.is_replied = True
        self.save()