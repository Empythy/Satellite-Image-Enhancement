"""
imageEnhance.py
YOUR WORKING FUNCTION
"""
import numpy as np
import cv2
from PIL import ImageEnhance
from PIL import Image

input_dir = 'input/input'
output_dir = 'output/output'

# you are allowed to import other Python packages above
##########################
def enhanceImage(img):
    # Inputs
    # inputImg: Input image, a 3D numpy array of row*col*3 in BGR format
    #
    # Output
    # outputImg: Enhanced image
    #
    #########################################################################
    # ADD YOUR CODE BELOW THIS LINE



    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(rgb)

    # contrast = ImageEnhance.Contrast(im_pil)
    # after_contrast = contrast.enhance(1.1)

    darken = ImageEnhance.Brightness(im_pil)
    after_darken = darken.enhance(0.95)

    sharpening = ImageEnhance.Sharpness(after_darken)
    after_sharp = sharpening.enhance(1.92)

    coloring = ImageEnhance.Color(after_sharp)
    after_color = coloring.enhance(2.0)

    contrast = ImageEnhance.Contrast(after_color)
    after_contrast = contrast.enhance(1)

    darken = ImageEnhance.Brightness(after_contrast)
    after_darken = darken.enhance(0.998)

    np_im=np.array(after_darken)

    opencv_image=cv2.cvtColor(np_im, cv2.COLOR_RGB2BGR)

    lab = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2LAB)
    # print(lab.shape)
    lab_planes = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.5,tileGridSize=(12,14))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab_planes[0] = clahe.apply(lab_planes[0])

    lab = cv2.merge(lab_planes)
    newImg = lab

    bgr = cv2.cvtColor(newImg, cv2.COLOR_LAB2BGR)

    # opencv_image = cv2.blur(bgr,(3,3))

    hsv = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HSV)
    # print(lab.shape)
    hsv_planes = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=2,tileGridSize=(7,7))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    newImg = hsv

    rgb = cv2.cvtColor(newImg, cv2.COLOR_HSV2RGB)

    im_pil = Image.fromarray(rgb)

    darken = ImageEnhance.Brightness(im_pil)
    after_darken = darken.enhance(0.998)

    sharpening = ImageEnhance.Sharpness(after_darken)
    after_sharp = sharpening.enhance(1.3)

    np_im=np.array(after_sharp)

    bgr=cv2.cvtColor(np_im, cv2.COLOR_RGB2BGR)

    outputImg = bgr

    # END OF YOUR CODE
    #########################################################################
    return outputImg
