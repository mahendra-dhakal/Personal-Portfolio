from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'phone', 'company']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add CSS classes and attributes to form fields
        self.fields['name'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Your Full Name *',
            'required': True
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'your.email@example.com *',
            'required': True
        })
        
        self.fields['subject'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'What would you like to discuss? *',
            'required': True
        })
        
        self.fields['message'].widget.attrs.update({
            'class': 'form-textarea',
            'placeholder': 'Tell me about your project, question, or how I can help you... *',
            'rows': 5,
            'required': True
        })
        
        self.fields['phone'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Your Phone Number (Optional)',
            'required': False
        })
        
        self.fields['company'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Your Company/Organization (Optional)',
            'required': False
        })

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Please provide a more detailed message (at least 10 characters).")
        return message

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Please enter your full name.")
        return name