from django.db import models
from PIL import Image
from django.conf import settings
import os


# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to="media/uploads")

    def crop(self, width, height):
        width = int(width)
        height = int(height)

        img = Image.open(os.path.join(settings.MEDIA_ROOT, self.image.name))

        # Get the current dimensions of the image
        current_width, current_height = img.size

        # Calculate coordinates for cropping
        left = (current_width - width) / 2
        top = (current_height - height) / 2
        right = (current_width + width) / 2
        bottom = (current_height + height) / 2

        # Crop the image
        cropped_img = img.crop((left, top, right, bottom))

        return cropped_img
