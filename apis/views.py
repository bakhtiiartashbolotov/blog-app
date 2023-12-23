from django.shortcuts import render

from rest_framework import generics 
from blog.models import Post
from .serializers import PostSerializer

class BlogAPIView(generics.ListCreateAPIView): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
