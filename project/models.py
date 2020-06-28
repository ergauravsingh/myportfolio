from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gaurav/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={
            'project_id':self.id
        })




class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='gaurav/images/blogimages', blank=True)
    date = models.DateField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={
            'blog_id':self.id
        })


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(default=now, editable=False)
    
    class Meta:
        unique_together = ['name', 'email' ,'message', 'subject']

    def __str__(self):
        return self.name
