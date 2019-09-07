"""
imageEnhance.py
YOUR WORKING FUNCTION
"""
import numpy as np
import cv2
from PIL import ImageEnhance,ImageFilter
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
    # ########################################################################
    # ADD YOUR CODE BELOW THIS LINE

    #Applying GaussianBlur
    img = cv2.GaussianBlur(img, (3,1),0)

    #Converting OpenCV BGR to RGB then convert to array form for pillow processing
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(rgb)

    #Pillow Sharp Enhancing
    sharpening = ImageEnhance.Sharpness(im_pil)
    after_sharp = sharpening.enhance(1.92)

    #Pillow Color Enhancing
    coloring = ImageEnhance.Color(after_sharp)
    after_color = coloring.enhance(2.0)

    #Pillow Brightness Enhancing
    darken = ImageEnhance.Brightness(after_color)
    after_darken = darken.enhance(0.998)

    #Converting Pillow Form back to OpenCV Form then converting to HSV form for CLAHE processing
    np_im=np.array(after_darken)
    opencv_image=cv2.cvtColor(np_im, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HSV)

    #Spltting HSV into H,S,V Channel
    hsv_planes = cv2.split(hsv)

    #Applying CLAHE on V Chanel, then merge HSV back together
    clahe = cv2.createCLAHE(clipLimit=2,tileGridSize=(7,7))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    newImg = hsv

    #Converting HSV back to RGB for Pillow Enhancement
    rgb = cv2.cvtColor(newImg, cv2.COLOR_HSV2RGB)
    im_pil = Image.fromarray(rgb)

    #Pillow Brightness Enhancing
    darken = ImageEnhance.Brightness(im_pil)
    after_darken = darken.enhance(0.998)

    #Pillow Sharpness Enhancement
    sharpening = ImageEnhance.Sharpness(after_darken)
    after_sharp = sharpening.enhance(1.3)

    #Converting RGB form (Pillow Form) back to BGR Form (Output original was BGR OpenCV Form)
    np_im=np.array(after_sharp)
    bgr=cv2.cvtColor(np_im, cv2.COLOR_RGB2BGR)
    outputImg = bgr
    # END OF YOUR CODE
    #########################################################################
    return outputImg
