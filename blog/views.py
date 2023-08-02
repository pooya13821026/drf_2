from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    def get_queryset(self):
        return Blog.objects.filter(is_active=True)


class BlogDetailView(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(Blog.objects.filter(is_active=True), pk=self.kwargs.get('pk'))
