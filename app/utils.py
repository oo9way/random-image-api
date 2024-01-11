from PIL import Image
from app.models import Images


def get_random_object():
    random_object = Images.objects.order_by("?").first()
    return random_object


def shrink_image(image_path, target_width, target_height):
    img = Image.open(image_path)

    if target_width and target_height and (target_width == target_height):
        current_width, current_height = img.size

        target_size = min(current_width, current_height)

        left = (current_width - target_size) // 2
        top = (current_height - target_size) // 2
        right = left + target_size
        bottom = top + target_size

        cropped_img = img.crop((left, top, right, bottom))
        img = cropped_img.resize((target_width, target_height))

    elif target_height and target_width:
        if target_width > target_height:
            # Resize by width
            aspect_ratio = img.width / img.height
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            # Resize by height
            aspect_ratio = img.height / img.width
            new_width = int(target_height / aspect_ratio)
            new_height = target_height

        img = img.resize((new_width, new_height))
        current_width, current_height = img.size

        # Calculate cropping coordinates to center the crop
        left = max(0, (current_width - target_width) // 2)
        top = max(0, (current_height - target_height) // 2)
        right = min(current_width, left + target_width)
        bottom = min(current_height, top + target_height)

        # Crop the image to the exact dimensions
        img = img.crop((left, top, right, bottom))

    img = img.convert("RGB")

    return img


def crop_image(image_path, width, height):
    img = Image.open(image_path)

    # Calculate cropping coordinates
    left = (img.width - width) // 2
    top = (img.height - height) // 2
    right = (img.width + width) // 2
    bottom = (img.height + height) // 2

    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    return cropped_img
