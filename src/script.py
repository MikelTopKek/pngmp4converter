from PIL import Image
import os


directory_base = r'./base_files'
directory_converted = r'./converted_files'


def convert():
    for filename in os.listdir(directory_base):
        if filename.endswith(".jpg"):
            im = Image.open(f'{directory_base}/{filename}')
            name = f'{directory_converted}/{filename}_converted.png'
            rgb_im = im.convert('RGB')
            rgb_im.save(name)
            print(os.path.join(directory_converted, filename))
            continue
        else:
            continue
