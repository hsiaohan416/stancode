"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """
    blank_img = SimpleImage.blank(figure_img.width, figure_img.height)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            combine_pixel = blank_img.get_pixel(x, y)
            figure_pixel = figure_img.get_pixel(x, y)
            bg_pixel = background_img.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > bigger*2:
                combine_pixel.red = bg_pixel.red
                combine_pixel.green = bg_pixel.green
                combine_pixel.blue = bg_pixel.blue
            else:
                combine_pixel.red = figure_pixel.red
                combine_pixel.green = figure_pixel.green
                combine_pixel.blue = figure_pixel.blue
    return blank_img


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
