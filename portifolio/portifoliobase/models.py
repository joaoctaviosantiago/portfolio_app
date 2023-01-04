from django.db import models
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1000)
    technologies = models.ManyToManyField('Technologies')
    created_date = models.DateTimeField(auto_now_add=True)

    def display_technologies(self):
        """Creates a string for the technologies. This is required to display technology in Admin."""
        return ', '.join(technology.name for technology in self.technologies.all())

    display_technologies.short_description = 'Technologies'

    def get_absolute_url(self):
        """Returns the url to access a particular project."""
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Technologies(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.title
