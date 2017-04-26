from PIL import Image
from inputs import InputType



def get_image_pixels(filepath):
    image = Image.open(filepath)
    width, height = image.size
    pixels = []
    for i in range(width):
        for j in range(height):
             pixel = image.getpixel((i,j))
             pixels.append(InputType((i,j),pixel))
    # image.show()
    return pixels


def create_new_picture(filepath, pixels, original_means):
    sorted_pixels = list(sorted(pixels, key=lambda k: [k.position[0],k.position[1]]))
    image = Image.new("RGB", (564,853))
    print("After finding new colors", original_means)
    for pixel in sorted_pixels:
        values = tuple(map(int, list(original_means[pixel.cluster_assignment])))
        image.putpixel(pixel.position, values)

    image.save("pictures/clustered/monabean.jpg")
