from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostEnListView.as_view(), name='post-list-en'),
    path('post/<int:pk>/', views.PostEnDetailView.as_view(), name='post-detail-en'),
]