"""
Adapted from Nick Parlante's Ghost assignment by Jerry Liao.

-----------------------------------------------
name: Sharon Tseng
file name: stanCodeshop.py

"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): distance between red, green, and blue pixel values

    """
    dist = math.sqrt((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    img_num = 0
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for i in range(len(pixels)):
        img_num += 1
        sum_red += pixels[i].red
        sum_green += pixels[i].green
        sum_blue += pixels[i].blue
    avg_red = sum_red//img_num
    avg_green = sum_green//img_num
    avg_blue = sum_blue//img_num
    return [avg_red, avg_green, avg_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    # Make a list of each color distance.
    dist_lst = []
    for i in range(len(pixels)):
        dist = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        dist_lst.append(dist)

    # Find the smallest color distance.
    # The default of min_dist is the maximum of color distance.(255*sqrt(3))
    min_dist = 442
    for i in range(len(dist_lst)):
        if dist_lst[i] < min_dist:
            min_dist = dist_lst[i]
            a = i                      # 'a' is the position of the smallest color distance in the list.
    return pixels[a]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # List all of the pixels of each pictures in the same list.
    img_pxl = []
    for i in range(len(images)):
        for x in range(images[i].width):
            for y in range(images[i].height):
                pxl = images[i].get_pixel(x, y)
                img_pxl.append(pxl)

    # i = total pixel number of one picture
    # The process in j is to get the same pixel position form each picture, and make them into pixels (List(img_pxl[j]).
    # Then get the best pixel, and append it to best (List(get_best_pixel(pixels)).
    pixels = []
    best = []
    for i in range(len(img_pxl)//len(images)):
        for j in range(0+i, len(img_pxl), len(img_pxl)//len(images)):
            pixels.append(img_pxl[j])
        best.append(get_best_pixel(pixels))
        pixels = []

    # Reconstruct the picture at blank (result).
    for x in range(result.width):
        for y in range(result.height):
            blank_pixel = result.get_pixel(x, y)
            blank_pixel.red = best[x * result.height + y].red
            blank_pixel.green = best[x * result.height + y].green
            blank_pixel.blue = best[x * result.height + y].blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
