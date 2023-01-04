from django.db import models

from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular project."""
        return reverse('post-detail-en', args=[str(self.id)])

    def __str__(self):
        return self.title

