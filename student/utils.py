from PIL import Image


def add_watermark(image_path, watermark_path):
    image = Image.open(image_path)
    watermark = Image.open(watermark_path)

    image_width, image_height = image.size
    watermark_width, watermark_height = watermark.size

    position = ((image_width - watermark_width) // 2, (image_height - watermark_height) // 2)

    # Apply the watermark
    image.paste(watermark, position, watermark)
    return image
