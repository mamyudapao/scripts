import sys
from PIL import Image


def convert_to_png(image_path, output_path, size=(32, 32)):
    img = Image.open(image_path)
    favicon = img.resize(size)
    favicon.save(output_path, "png", optimize=True)


convert_to_png(sys.argv[1], sys.argv[2])
