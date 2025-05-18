from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()  
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=300)  

    def __str__(self):
        return self.title



