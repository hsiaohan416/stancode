"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    original_mt = SimpleImage(filename)
    blank_img = SimpleImage.blank(original_mt.width, original_mt.height*2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            old_pixel = original_mt.get_pixel(x, y)
            new_pixel_1 = blank_img.get_pixel(x, y)
            new_pixel_2 = blank_img.get_pixel(x, blank_img.height-y-1)
            new_pixel_1.red = old_pixel.red
            new_pixel_1.green = old_pixel.green
            new_pixel_1.blue = old_pixel.blue
            new_pixel_2.red = old_pixel.red
            new_pixel_2.green = old_pixel.green
            new_pixel_2.blue = old_pixel.blue
    return blank_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
