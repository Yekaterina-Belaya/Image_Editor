from PIL import Image, ImageEnhance, ImageFilter
import os

path = "C:/Users/belos/Desktop/бэк/for PET_Image_editor/edit"
pathOut = "C:/Users/belos/Desktop/бэк/for PET_Image_editor/edited"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SMOOTH).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{clean_name}_edited.jpg")

