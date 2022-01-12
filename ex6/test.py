# from  ex6 import *

# # candidates_list = (5,6,7,2)
# # num_candidates = 3
# # # c = [0,0,0]
# # #
# # # for i in range(len(k)):
# # #     c[i] += k[i]
# # # print(c)
# # #
# # # for i in range(len(c)):
# # #     c[i] /= 2
# # #
# # # print(c)
# #
# #
# # # if averages[i] == objective_colour and len(candidates_list) != num_candidates:
# # #     candidates_list.append(tiles[i])
# # # print(k)
# # # a = sorted(k)
# # # a = a[0:2]
# # # print(a)
# #
# # sorted_candidates_list = sorted(candidates_list)
# # print(num_candidates)
# # sorted_candidates_list = sorted_candidates_list[0:num_candidates]
# #
# # print(sorted_candidates_list)
#
# def average(image):
#     img_height = len(image[0])
#     img_width = len(image[0][0])
#     total = [0, 0, 0]
#     number_of_pixels = img_width * img_height
#
#     for i in range(img_height):
#         for j in range(img_width):
#             for k in range(len(image[0][i][j])):
#                 total[k] += image[0][i][j][k]
#
#     for i in range(len(total)):
#         total[i] /= number_of_pixels
#
#     return tuple(total)
#
# print(average([[[(20, 40, 60), (20, 40, 60), (20, 40, 60)], [(60, 41, 20), (60, 41, 20), (60, 41, 20)]]]))

im1 = [[(20,40,60),(20,40,60),(20,40,60)],
       [(20,40,60),(20,40,60),(20,40,60)]]

im2 = [[(20,40,60),(25,47,69),(10,20,30)],
       [(10,50,60),(30,40,50),(20,30,70)]]

im3 = [[(20,40,60),(25,47,69)],
       [(10,50,60),(30,40,50)],
       [(10,20,30),(20,30,70)]]

im4 = [[(20,40,60),(20,40,60),(20,40,60)],
       [(60,41,20),(60,41,20),(60,41,20)]]



# def compare(image1, image2):
#     height = min(len(image1), len(image2))
#     width = min(len(image1[0]), len(image2[0]))
#     distance = ZERO
#
#     for i in range(height):
#         for j in range(width):
#             distance += compare_pixel(image1[i][j], image2[i][j])
#     return distance

def get_piece(image, upper_left, size):
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
                row_output.append(image[start_height + i][start_width + j])
        if row_output != list():
            output_img.append(row_output)

    return output_img


print(get_piece(im2,(1,2),(1,1)))
print(get_piece(im2,(1,2),(2,2)))