"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    blank_img = SimpleImage.blank(img.width, img.height)
    for x in range(1, img.width-1):
        for y in range(1, img.height-1):
            left1_pixel = img.get_pixel(x-1, y-1)
            left2_pixel = img.get_pixel(x-1, y)
            left3_pixel = img.get_pixel(x-1, y+1)
            center1_pixel = img.get_pixel(x, y-1)
            center2_pixel = img.get_pixel(x, y)
            center3_pixel = img.get_pixel(x, y+1)
            right1_pixel = img.get_pixel(x+1, y-1)
            right2_pixel = img.get_pixel(x+1, y)
            right3_pixel = img.get_pixel(x+1, y+1)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = (left1_pixel.red + left2_pixel.red + left3_pixel.red + center1_pixel.red + center2_pixel.red
                             + center3_pixel.red + right1_pixel.red + right2_pixel.red + right3_pixel.red) // 9
            new_pixel.green = (left1_pixel.green + left2_pixel.green + left3_pixel.green + center1_pixel.green +
                               center2_pixel.green + center3_pixel.green + right1_pixel.green + right2_pixel.green +
                               right3_pixel.green) // 9
            new_pixel.blue = (left1_pixel.blue + left2_pixel.blue + left3_pixel.blue + center1_pixel.blue +
                              center2_pixel.blue + center3_pixel.blue + right1_pixel.blue + right2_pixel.blue +
                              right3_pixel.blue) // 9
    for x in range(1):
        for y in range(1, img.height-1):
            """edge x=0"""
            edge1_pixel = img.get_pixel(x, y-1)
            edge2_pixel = img.get_pixel(x, y)
            edge3_pixel = img.get_pixel(x, y+1)
            edge4_pixel = img.get_pixel(x+1, y-1)
            edge5_pixel = img.get_pixel(x+1, y)
            edge6_pixel = img.get_pixel(x+1, y+1)
            new_pixel = blank_img.get_pixel(x, y)
            new_pixel.red = (edge1_pixel.red + edge2_pixel.red + edge3_pixel.red + edge4_pixel.red + edge5_pixel.red +
                             edge6_pixel.red) // 6
            new_pixel.green = (edge1_pixel.green + edge2_pixel.green + edge3_pixel.green + edge4_pixel.green +
                               edge5_pixel.green + edge6_pixel.green) // 6
            new_pixel.blue = (edge1_pixel.blue + edge2_pixel.blue + edge3_pixel.blue + edge4_pixel.blue +
                              edge5_pixel.blue + edge6_pixel.blue) // 6
    for x in range(img.width-1, img.width):
        for y in range(1, img.height-1):
            """edge x=width-1"""
            edge1_pixel = img.get_pixel(x-1, y-1)
            edge2_pixel = img.get_pixel(x-1, y)
            edge3_pixel = img.get_pixel(x-1, y+1)
            edge4_pixel = img.get_pixel(x, y-1)
            edge5_pixel = img.get_pixel(x, y)
            edge6_pixel = img.get_pixel(x, y+1)
            new_pixel = img.get_pixel(x, y)
            new_pixel.red = (edge1_pixel.red + edge2_pixel.red + edge3_pixel.red + edge4_pixel.red + edge5_pixel.red +
                             edge6_pixel.red) // 6
            new_pixel.green = (edge1_pixel.green + edge2_pixel.green + edge3_pixel.green + edge4_pixel.green +
                               edge5_pixel.green + edge6_pixel.green) // 6
            new_pixel.blue = (edge1_pixel.blue + edge2_pixel.blue + edge3_pixel.blue + edge4_pixel.blue +
                              edge5_pixel.blue + edge6_pixel.blue) // 6
    for x in range(1, img.width-1):
        for y in range(1):
            """edge y=0"""
            edge1_pixel = img.get_pixel(x-1, y)
            edge2_pixel = img.get_pixel(x, y)
            edge3_pixel = img.get_pixel(x+1, y)
            edge4_pixel = img.get_pixel(x-1, y+1)
            edge5_pixel = img.get_pixel(x, y+1)
            edge6_pixel = img.get_pixel(x+1, y+1)
            new_pixel = img.get_pixel(x, y)
            new_pixel.red = (edge1_pixel.red + edge2_pixel.red + edge3_pixel.red + edge4_pixel.red + edge5_pixel.red +
                             edge6_pixel.red) // 6
            new_pixel.green = (edge1_pixel.green + edge2_pixel.green + edge3_pixel.green + edge4_pixel.green +
                               edge5_pixel.green + edge6_pixel.green) // 6
            new_pixel.blue = (edge1_pixel.blue + edge2_pixel.blue + edge3_pixel.blue + edge4_pixel.blue +
                              edge5_pixel.blue + edge6_pixel.blue) // 6
    for x in range(1, img.width-1):
        for y in range(img.height-1, img.height):
            """edge y=height-1"""
            edge1_pixel = img.get_pixel(x-1, y-1)
            edge2_pixel = img.get_pixel(x, y-1)
            edge3_pixel = img.get_pixel(x+1, y-1)
            edge4_pixel = img.get_pixel(x-1, y)
            edge5_pixel = img.get_pixel(x, y)
            edge6_pixel = img.get_pixel(x+1, y)
            new_pixel = img.get_pixel(x, y)
            new_pixel.red = (edge1_pixel.red + edge2_pixel.red + edge3_pixel.red + edge4_pixel.red + edge5_pixel.red +
                             edge6_pixel.red) // 6
            new_pixel.green = (edge1_pixel.green + edge2_pixel.green + edge3_pixel.green + edge4_pixel.green +
                               edge5_pixel.green + edge6_pixel.green) // 6
            new_pixel.blue = (edge1_pixel.blue + edge2_pixel.blue + edge3_pixel.blue + edge4_pixel.blue +
                              edge5_pixel.blue + edge6_pixel.blue) // 6
     
    return blank_img



def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
