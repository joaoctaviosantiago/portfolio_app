from django.contrib import admin

from .models import Project, Technologies, Contact

# Register your models here.

admin.site.register(Project)
admin.site.register(Technologies)
admin.site.register(Contact)