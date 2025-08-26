from django.contrib import admin
from .models import Skill, Project, Achievement, Experience, ContactMessage

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['proficiency', 'is_featured', 'order']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'proficiency', 'icon')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        })
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_featured', 'order', 'created_at']
    list_filter = ['status', 'is_featured', 'is_personal']
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['status', 'is_featured', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subtitle', 'short_description')
        }),
        ('Detailed Description', {
            'fields': ('description', 'key_features', 'challenges', 'learnings')
        }),
        ('Links & Media', {
            'fields': ('demo_url', 'github_url', 'case_study_url', 'image', 'video_url')
        }),
        ('Technical Details', {
            'fields': ('status', 'technologies', 'tech_tags')
        }),
        ('Timeline', {
            'fields': ('start_date', 'completion_date')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'is_personal', 'order')
        })
    )
    
    filter_horizontal = ['technologies']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'organization', 'date_achieved', 'is_featured', 'order']
    list_filter = ['category', 'is_featured', 'date_achieved']
    search_fields = ['title', 'organization', 'description']
    list_editable = ['is_featured', 'order']
    date_hierarchy = 'date_achieved'
    ordering = ['order', '-date_achieved']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'organization', 'date_achieved')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Verification', {
            'fields': ('certificate_url', 'credential_id')
        }),
        ('Display Options', {
            'fields': ('icon', 'is_featured', 'order')
        })
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'employment_type', 'start_date', 'end_date', 'is_current', 'is_featured', 'order']
    list_filter = ['employment_type', 'is_featured', 'start_date']
    search_fields = ['position', 'company', 'description']
    list_editable = ['is_featured', 'order']
    date_hierarchy = 'start_date'
    ordering = ['order', '-start_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'position', 'employment_type', 'location')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Links & Media', {
            'fields': ('company_url', 'company_logo')
        }),
        ('Technologies', {
            'fields': ('technologies_used',)
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        })
    )
    
    filter_horizontal = ['technologies_used']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read', 'is_replied']
    list_filter = ['is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at', 'ip_address', 'user_agent']
    list_editable = ['is_read', 'is_replied']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Additional Information', {
            'fields': ('phone', 'company'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_read', 'is_replied')
        }),
        ('System Information', {
            'fields': ('created_at', 'ip_address', 'user_agent'),
            'classes': ('collapse',)
        })
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['name', 'email', 'subject', 'message', 'phone', 'company']
        return self.readonly_fields

# Customize the admin site header
admin.site.site_header = "Mahendra Dhakal Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Your Portfolio Content"