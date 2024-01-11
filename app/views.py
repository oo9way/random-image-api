import os
from io import BytesIO

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from app.utils import get_random_object, shrink_image
from app.tasks import download_images


class HomePageView(TemplateView):
    template_name = "home.html"


def photo_api(request):
    image_filename = get_random_object().image.name
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    target_width = int(request.GET.get("width", 0))
    target_height = int(request.GET.get("height", 0))

    resized_image = shrink_image(image_path, target_width, target_height)

    image_stream = BytesIO()
    resized_image.save(image_stream, format="JPEG")

    image_stream.seek(0)

    response = HttpResponse(image_stream.getvalue(), content_type="image/jpeg")

    return response


def get_random_images(request):
    if request.method == "POST":
        download_images.delay()
    return render(request, "download_images.html")
