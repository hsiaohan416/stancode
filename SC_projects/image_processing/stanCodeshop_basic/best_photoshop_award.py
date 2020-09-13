"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
"""
from simpleimage import SimpleImage


def main():
    pangpang = SimpleImage('images/pang.jpg')
    pangpang.show()
    background = SimpleImage('images/ryan.jpg')
    background.show()
    pang_small = shrink(pangpang)
    # make the size of the photo into 1/4
    pang_small = shrink(pang_small)
    pang_small = shrink(pang_small)
    result = de_bg(pang_small, background)
    result.show()


def shrink(figure_img):
    # shrink the photo with green background
    small_img = SimpleImage.blank(figure_img.width//2, figure_img.height//2)
    if figure_img.width % 2 == 1 or figure_img.height % 2 == 1:
        for x in range(0, figure_img.width-1, 2):
            for y in range(0, figure_img.height-1, 2):
                pixel_1 = figure_img.get_pixel(x, y)
                pixel_2 = figure_img.get_pixel(x+1, y)
                pixel_3 = figure_img.get_pixel(x, y+1)
                pixel_4 = figure_img.get_pixel(x+1, y+1)
                small_pixel = small_img.get_pixel(x//2, y//2)
                small_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red)//4
                small_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
                small_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
    else:
        for x in range(0, figure_img.width, 2):
            for y in range(0, figure_img.height, 2):
                pixel_1 = figure_img.get_pixel(x, y)
                pixel_2 = figure_img.get_pixel(x+1, y)
                pixel_3 = figure_img.get_pixel(x, y+1)
                pixel_4 = figure_img.get_pixel(x+1, y+1)
                small_pixel = small_img.get_pixel(x//2, y//2)
                small_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red)//4
                small_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
                small_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
    return small_img


def de_bg(green_bg_photo, background):
    blank_img = SimpleImage.blank(background.width, background.height)
    for x in range(pang_small.width):
        for y in range(pang_small.height):
            pang_pixel = pang_small.get_pixel(x, y)
            bg_pixel = background.get_pixel(x+250, y+148)
            new_pixel = blank_img.get_pixel(x+250, y+148)
            rgb_sum = pang_pixel.red + pang_pixel.green + pang_pixel.blue
            avg = rgb_sum // 3
            if pang_pixel.green > avg * 1.25:
                new_pixel.red = bg_pixel.red
                new_pixel.green = bg_pixel.green
                new_pixel.blue = bg_pixel.blue
            else:
                new_pixel.red = pang_pixel.red
                new_pixel.green = pang_pixel.green
                new_pixel.blue = pang_pixel.blue
            if rgb_sum < 120:
                new_pixel.red = pang_pixel.red
                new_pixel.green = pang_pixel.green
                new_pixel.blue = pang_pixel.blue
    for x in range(250):
        for y in range(background.height):
            bg_pixel = background.get_pixel(x, y)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = bg_pixel.red
            new_pixel.green = bg_pixel.green
            new_pixel.blue = bg_pixel.blue
    for x in range(250 + pang_small.width, background.width):
        for y in range(background.height):
            bg_pixel = background.get_pixel(x, y)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = bg_pixel.red
            new_pixel.green = bg_pixel.green
            new_pixel.blue = bg_pixel.blue
    for x in range(250, 250 + pang_small.width):
        for y in range(0, 148):
            bg_pixel = background.get_pixel(x, y)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = bg_pixel.red
            new_pixel.green = bg_pixel.green
            new_pixel.blue = bg_pixel.blue

    return blank_img











    # for x in range(bg_img.width):
    #     for y in range(bg_img.height):





if __name__ == '__main__':
    main()
