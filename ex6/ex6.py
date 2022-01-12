############################################################
# FILE : ex6.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION :  At README
############################################################

import math
from copy import deepcopy
from mosaic import *
import sys
from PIL import Image

NUM_OF_COLORS = 3
ZERO = 0
MAX_DISTANCE = 266
NUM_OF_ARGUMENTS = 6
WRONG_INPUT_MSG = "Wrong number of parameters. The correct usage is: " + "\n"\
                  + "ex6.py <image_source> <images_dir> <output_name> " \
                    "<tile_height> <num_candidates>"


def compare_pixel(pixel1, pixel2):
    """ Takes two pixels given by a tuple and find the distance between them
     by the formula |r1-r2| + |b1 - b2| + |g1 - g2| """
    average_colour = ZERO
    for i in range(NUM_OF_COLORS):
        average_colour += math.fabs(pixel1[i] - pixel2[i])
    return average_colour


def compare(image1, image2):
    """Takes two images and by comparing pixel-pixel in them finds the distance
     between the two"""
    height = min(len(image1), len(image2))
    width = min(len(image1[0]), len(image2[0]))
    # makes sure that we wont exit from the boundaries of none of the images
    distance = ZERO

    for i in range(height):
        for j in range(width):
            distance += compare_pixel(image1[i][j], image2[i][j])
    return distance


def get_piece(image, upper_left, size):
    """cuts a piece from the image by getting a starting point of the
    upper-left corner and size """
    img_height = len(image)
    img_width = len(image[0])
    start_height = upper_left[0]
    start_width = upper_left[1]
    cut_height = size[0]
    cut_width = size[1]
    output_img = list()

    for i in range(cut_height):
        row_output = list()
        for j in range(cut_width):
            if (start_height + i < img_height) and (start_width + j < img_width):
                # checks we wont exit from the boundaries of the image
                row_output.append(image[start_height + i][start_width + j])
        if row_output != list():  # in case we still in the rows boundaries but
                                  # out of the colms boundaries
            output_img.append(row_output)

    return output_img


def set_piece(image, upper_left, piece):
    """set the piece to the right place in the image pixel by pixel"""
    img_height = len(image)
    img_width = len(image[0])
    start_height = upper_left[0]
    start_width = upper_left[1]
    switch_height = len(piece)
    switch_width = len(piece[0])

    for i in range(switch_height):
        for j in range(switch_width):
            if (start_height + i < img_height) and (start_width + j < img_width):
                # staying in the boundaries of the big image
                image[start_height + i][start_width + j] = piece[i][j]
                # entering the right pixel in the tile to the right place to
                # the big image with respect to the given start point


def average(image):
    """finds the average colour of an image by summing all the pixels and
     devise by the number of the pixels"""
    img_height = len(image)
    img_width = len(image[0])
    total = [0, 0, 0]
    number_of_pixels = img_width * img_height

    for i in range(img_height):
        for j in range(img_width):
            for k in range(len(image[i][j])):
                total[k] += image[i][j][k]  # summing all the red green blue

    for i in range(len(total)):
        total[i] /= number_of_pixels  # devise each colour by number of pixels

    return tuple(total)


def preprocess_tiles(tiles):
    """find the average colour of each tile in the list and saves it"""
    avg_list = list()
    for i in range(len(tiles)):
        avg_list.append(average(tiles[i]))
    return avg_list


def get_best_tiles(objective, tiles, averages, num_candidates):
    """finds the most similar tiles to a given tile and saves them in a list"""
    candidates_list = list()
    tiles_list = list()
    num_candidates = int(num_candidates)
    objective_colour = average(objective)  # the colour ro compare to

    for i in range(len(averages)):
        # comparing each and every tile to our objective
        candidates_list.append(compare_pixel(objective_colour, averages[i]))

    sorted_candidates_list = sorted(candidates_list)
    sorted_candidates_list = sorted_candidates_list[0:num_candidates]
    # by sorting the list and slicing it in the number of tiles I want I get
    #  the num_candidate tiles that fit the most

    for i in range(len(candidates_list)):
        if candidates_list[i] in sorted_candidates_list:
            tiles_list.append(tiles[i])
    # in each iteration I check the index of the best tiles and add them to the
    #  final list
    return tiles_list


def choose_tile(piece, tiles):
    """finds the most similar tile to a given piece by comparing the pixels"""
    distance = compare(piece, tiles[0])  # the basic distance to compare to
    for i in range(len(tiles)):
        check = compare(piece, tiles[i])  # comparing each tile to the piece
        if check <= distance:
            distance = check
            index = i  # saves the index of the minimal distance
    return tiles[index]


def make_mosaic(image, tiles, num_candidates):
    """cut a piece form the image, finds the best mach from a list of tiles
     and set that piece in the right place in the image"""
    work_image = deepcopy(image)
    image_height = len(image)
    image_width = len(image[0])
    piece_height = len(tiles[0])
    piece_width = len(tiles[0][0])
    avg_list = preprocess_tiles(tiles)

    for i in range(0, image_height, piece_height):
        for j in range(0, image_width, piece_width):
                piece = get_piece(image, (i, j), (piece_height, piece_width))
                candidates = get_best_tiles(piece, tiles, avg_list, num_candidates)
                tile = choose_tile(piece, candidates)
                set_piece(work_image, (i, j), tile)

    return work_image


if __name__ == "__main__":
    if len(sys.argv) == NUM_OF_ARGUMENTS:
        image_source = sys.argv[1]
        image_dir = sys.argv[2]
        output_name = sys.argv[3]
        tile_height = sys.argv[4]
        tile_height = int(tile_height)
        num_candidates = sys.argv[5]
        my_image = load_image(image_source)
        tiles = build_tile_base(image_dir, tile_height)
        output_image = make_mosaic(my_image, tiles, num_candidates)
        save(output_image, output_name)
    elif len(sys.argv) != NUM_OF_ARGUMENTS:
        print(WRONG_INPUT_MSG)
