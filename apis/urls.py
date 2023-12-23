from django.urls import path
from .views import BlogAPIView

urlpatterns = [
    path("", BlogAPIView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetails.as_view(), name="blog_details"),

]
