import os
import urllib.request
from PIL import Image,ImageColor,ImageFilter,ImageOps




def convert_to_pencil_sketch(image_path, save_path):
    image = Image.open(image_path).convert("L")
    image = image.filter(ImageFilter.CONTOUR)
    image = ImageOps.invert(image)
    image.save(save_path)

root_dir = "data"

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'resized.jpg':
            print('inside resized')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "pencil_sketch_" + file)
            convert_to_pencil_sketch(image_path, save_path)
