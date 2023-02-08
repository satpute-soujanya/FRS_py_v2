import os
import urllib.request
from PIL import Image,ImageColor,ImageFilter,ImageOps


def download_images(csv_file, parent_folder):
    with open(csv_file, 'r') as f:
        lines = f.readlines()
        
    for line in lines[1:]: # skip the first line (header)
        items = line.strip().split(',')
        folder_name = items[0]
        image_url = items[1]
        folder_path = os.path.join(parent_folder, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # image_path = os.path.join(folder_path,"original.jpg")

        # urllib.request.urlretrieve(image_url, image_path)
download_images('datacreation.csv', 'data')

def convert_to_pencil_sketch(image_path, save_path):
    image = Image.open(image_path).convert("L")
    image = image.filter(ImageFilter.CONTOUR)
    image = ImageOps.invert(image)
    image.save(save_path)
def resize_with_aspect_ratio(image, size,save_path):
    imgoriginal = Image.open(image)
    resizedImage= imgoriginal.copy()
    resizedImage.thumbnail(size)
    resizedImage.save(save_path)
    return resizedImage
root_dir = "data"
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'original.jpg':
            print('inside original')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "resized.jpg")
            resize_with_aspect_ratio(image_path,(128,128) ,save_path)
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'resized.jpg':
            print('inside resized')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "pencil_sketch_" + file)
            convert_to_pencil_sketch(image_path, save_path)
