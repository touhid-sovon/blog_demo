from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeListView.as_view(), name="home"),
    path('post-detail/<int:pk>', views.BlogDetailView.as_view(), name="post-detail"),
]
