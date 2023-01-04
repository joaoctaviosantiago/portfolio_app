from django.shortcuts import render
from django.views import generic
from django.utils.translation import get_language, activate, gettext
from django.urls import reverse_lazy

from .models import Project, Contact

# Create your views here.

# EN-US

def index_en(request):
    context={}
    return render(request, 'base_template.html', context)

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 3

    def get_queryset(self):
        return Project.objects.order_by('-created_date')


class ProjectDetailView(generic.DetailView):
    model = Project


class ContactCreate(generic.CreateView):
    model = Contact
    fields = ['name', 'email', 'title', 'message']
    success_url = reverse_lazy('index')