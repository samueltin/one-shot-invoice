import os
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


IMAGE_DIR=os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'data', 'template')
IMAGE_LIST=os.listdir(IMAGE_DIR)

display_img=False

def _pick_image():
    idx = random.choice(range(0, len(IMAGE_LIST)-1, 1))
    img_file = os.path.join(IMAGE_DIR, IMAGE_LIST[idx])
    img = Image.open(img_file)
    _plot_image(img_file)

    return img

def _plot_image(img_file):
    if display_img:
        image = mpimg.imread(img_file)
        plt.imshow(image)
        plt.show()

def _draw_text(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0), "Hello Hello Hello World World", (0, 0, 0), font=font)
    # img.save('hello.jpg')
    img.show()


def main():
    img = _pick_image()
    _draw_text(img)

if __name__ == "__main__":
    main()