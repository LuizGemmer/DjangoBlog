from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Post

# Create your views here.
class HomeView(generic.ListView):
    model=Post
    template_name='blogApp/home.html'
    context_object_name="posts"

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.all()
