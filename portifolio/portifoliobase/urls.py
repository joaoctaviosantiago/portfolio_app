from django.urls import path
from django.utils.translation import gettext as _

from . import views

urlpatterns = [
    path('', views.index_en, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('contact/', views.ContactCreate.as_view(), name='contact-create'),
]