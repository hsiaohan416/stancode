"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    old_img = SimpleImage("images/poppy.png")
    blank_img = SimpleImage.blank(old_img.width//2, old_img.height//2)
    for x in range(0, old_img.width, 2):
        for y in range(0, old_img.height, 2):
            pixel_1 = old_img.get_pixel(x, y)
            pixel_2 = old_img.get_pixel(x+1, y)
            pixel_3 = old_img.get_pixel(x, y+1)
            pixel_4 = old_img.get_pixel(x+1, y+1)
            new_pixel = blank_img.get_pixel(x//2, y//2)
            new_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red)//4
            new_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
            new_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
    return blank_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
