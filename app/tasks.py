from celery import shared_task
from app.models import Images
import requests
import tempfile
import time
import threading

from django.core import files


@shared_task
def download_images():
    threads = []
    num_threads = 20

    images = []

    def download_image():
        url = "https://picsum.photos/200/300"
        response = requests.get(url, stream=True)

        lf = tempfile.NamedTemporaryFile()
        for block in response.iter_content(1024 * 8):
            if not block:
                raise FileNotFoundError
            lf.write(block)

        file_name = url.split("/")[-1] + ".png"
        image = Images()
        image.image.save(file_name, files.File(lf), save=False)
        images.append(image)

    for _ in range(num_threads):
        thread = threading.Thread(target=download_image)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    Images.objects.bulk_create(images)
