# from PIL import Image
#
# im = Image.open('pictures/original\monobean.jpg')
# im.show()
from random import randint
import image_parser as ip
from kmeans import Kmeans

def get_random_means():
    return [(randint(0,255),randint(0,255), randint(0,255)) for i in range(3)]

if __name__ == "__main__":
    image_path = "pictures/original/bird.jpg"
    pixels = ip.get_image_pixels(image_path)
    init_means = get_random_means()
    kmeans = Kmeans(pixels, init_means)
    kmeans.start()
    clusted_pixels = kmeans.inputs

    new_picture = "pictures/clustered/bird.jpg"
    ip.create_new_picture(new_picture, clusted_pixels, init_means)
