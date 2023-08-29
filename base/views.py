from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
# Create your views here.


class HomeListView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'
    context_object_name = "post"


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post-new.html'
    fields = [
        'title',
        'author',
        'body'
    ]
    success_url = reverse_lazy('home')


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = [
        'title',
        'body'
    ]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
