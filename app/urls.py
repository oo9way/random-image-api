from django.urls import path
from app.views import HomePageView, photo_api, get_random_images
urlpatterns = [
    path("", HomePageView.as_view()),
    path("photo/", photo_api, name="photo"),
    path("image-post/", get_random_images),
]
