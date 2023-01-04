from django.shortcuts import render
from django.views import generic

from .models import Post


# Create your views here.

# BLOG EN-US

class PostEnListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list_en.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostEnDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail_en.html'




# BLOG PT-BR

class PostPtListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list_pt.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostPtDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail_pt.html'