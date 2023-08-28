from django.views.generic import ListView, TemplateView, DetailView
from .models import *
# Create your views here.


class HomeListView(ListView):
    model = Post
    template_name = 'base/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'base/post-details.html'
    context_object_name = "post"
