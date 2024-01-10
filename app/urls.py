from django.urls import path
from app.views import index, HomePageView, get_random_images
urlpatterns = [
    path("", HomePageView.as_view()),
    path("photo/", index, name="photo"),
    path("image-post/", get_random_images),
]
