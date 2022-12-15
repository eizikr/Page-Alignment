import sys
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import math


def straightensPage():
    INPUT_PATH ,OUTPUT_PATH = (sys.argv[1]), (sys.argv[2])
    #   Read image from input path
    img = cv.imread(INPUT_PATH)

    #   Binarize the image (make pixels either 0 or 255) 
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur_img = cv.blur(img_grey, (20, 20))
    _, binary_img = cv.threshold(blur_img, 95, 255, cv.THRESH_OTSU)
    
    #   Find the largest contour in the image.
    cnts, _ = cv.findContours(binary_img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    biggest_contour = get_biggest_contour(cnts)

    #   Find the bounding rectangle of the contour with minimum area
    box = cv.minAreaRect(biggest_contour)
    boxPts = np.int0(cv.boxPoints(box))

    #   Calculate the height and width of the page
    height,width = calculate_height_and_weigth(boxPts)

    #   Define the transformation matrix the four corners of the page will be mapped to four corners in the output image.
    old_points = [[0,0],[width-1,0],[width-1,height-1],[0,height]]
    output_corners = np.float32(old_points)                       
    original_corners = np.float32(boxPts)                          
    transformation_matrix = cv.getPerspectiveTransform(original_corners,output_corners)

    #   Applies a perspective transformation to an image.
    final_img = cv.warpPerspective(img,transformation_matrix,(width,height))

    #   Write new image to output path
    cv.imwrite(OUTPUT_PATH, final_img)

    #   If you want to show on screen
    # plt.imshow(cv.cvtColor(final_img, cv.COLOR_RGB2BGR))
    # plt.show()

def get_biggest_contour(contours):
    '''This function returns the largest contour'''
    biggest_contour = None
    biggest_area = 0
    for contour in contours:
        
        area = cv.contourArea(contour)

        if area > biggest_area:
            biggest_contour = contour
            biggest_area = area
    return biggest_contour

def calculate_height_and_weigth(boxPts):
    '''
    This function calculating the image size by the boxPts indexes
    boxPts[0]######boxPts[1]
    ########################
    ##########PAGE##########
    ########################
    boxPts[3]######boxPts[2]
    '''
    top_left=list(boxPts[0])
    top_right=list(boxPts[1])
    bottom_right=list(boxPts[2])
    bottom_left=list(boxPts[3]) 

    #   Calculate image sizes
    height_distances = math.dist(top_right, bottom_right) + math.dist(top_left, bottom_left)
    width_distances = math.dist(top_right,top_left) + math.dist(bottom_right,bottom_left)
    both_sides = (int(height_distances/2) , int(width_distances/2))
    #   Return height and weigth (Heigth bigger then Weigth)
    return max(both_sides), min(both_sides) 


if __name__ == '__main__':
    straightensPage()