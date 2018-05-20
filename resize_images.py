# tool for resizing images to wanted size

from pathlib import Path

import PIL
from PIL import Image

# configure base height of all images
BASEHEIGHT = 500

def resize(img_path):
    """
    takes images path and save resized image cropped directory
    """
    img = Image.open(img_path)
    hpercent = (BASEHEIGHT / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, BASEHEIGHT), PIL.Image.ANTIALIAS)
    img.save(f"cropped/{img_path}")


def main():
    images_path = Path('load')
    cropped_path = Path('cropped')
    if images_path.exists():

        if not cropped_path.exists():
            cropped_path.mkdir(parents=True, exist_ok=True)
            folders = [x for x in images_path.glob('**/*') if not x.is_file()]
            for f in folders:
                p = cropped_path / f
                p.mkdir(parents=True, exist_ok=True)

        images = list(images_path.glob('**/*.jpg'))
        if images:
            for image_path in images:
                resize(str(image_path))
        else:
            print("No '.jpg' files found in 'images' folder!")
    else:
        print("No 'images' folder found!")

if __name__ == '__main__':
    main()
