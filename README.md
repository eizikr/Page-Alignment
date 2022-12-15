# Page-Alignment
# Description:
    - This program was created as part of course 'Image processing and computer vision' (Homework no.2).
    - The program is using 'OpenCV' package that takes a photo of a rectangular page and straightens the photo.
    - Steps:
        1. Binarize the image.
        2. Find the largest contour in the image.
        3. Find the bounding rectangle of the contour with minimum area.
        4. Calculate the height and width of the page.
        5. Define the transformation matrix the four corners of the page will be mapped to four corners in the output image.
        6. Applies a perspective transformation to an image.
        7. Write new image to output path.

# Assumptions:
    - A page is the basic object in the image.
    - The page photographed is a rectangular page.
    - The height of the page is greater than its width.
    - The page is brighter than the background on which it was photographed.


# Environment:
    This program was created to be use in windows 11 OS.
    To use this program you requied:
    -   Installed python 3.11.0 (requied)
    -   Create environment -> 'python -m venv opencv-env' (optional)
        * Activate environment -> '.\opencv-env\Scripts\activate'
        * Deactivate -> 'deactivate'
    -   Install openCV package -> pip install opencv-contrib-python matplotlib

# How to Run Your Program:
    - Activate opencv-env environment -> .\opencv-env\Scripts\activate
    - run the program whith 2 input (image path) , (output path)
        * example: "python straightensPage.py input\IMG-3763.jpg output\my_new.jpg"

ENJOY!
