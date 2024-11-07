from django.db import models

# Create your models here.
class Article(models.Model):
    type_of = models.CharField(max_length=7,default="article")
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='media/images')
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    path=models.SlugField(max_length=150,unique=True,null=True,blank=True)
    comments_count = models.PositiveIntegerField(null=True,blank=True)
    public_reactions_count = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    positive_reactions_count = models.PositiveIntegerField(blank=True,null=True)
    negative_reactions_count = models.PositiveIntegerField(blank=True,null=True)
    reading_time_minutes = models.PositiveIntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    comment = models.CharField(max_length=250,blank=True,null=True)