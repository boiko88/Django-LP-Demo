from django.db import models

class PersonalBlog(models.Model):
    blog_name = models.CharField(max_length=100, blank=False)
    blog_description= models.CharField(max_length=300, blank=False)
    
    
    def __str__(self):
        return f"{self.blog_name}"