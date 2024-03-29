import base64
from io import BytesIO
from PIL import Image

def process_image(image_data):
    # Convert base64 image data to PIL Image
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    # Process the image (for example, calculate the size)
    width, height = image.size
    size_label = "Large" if width * height > 100000 else "Small"

    return size_label
