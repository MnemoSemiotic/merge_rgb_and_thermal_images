import numpy as np

from skimage.color import rgb2gray, rgb2hsv, hsv2rgb, rgb2lab, lab2rgb
from skimage import img_as_ubyte

# import utility functions
from merging_utilities.img_utils import *
from merging_utilities.os_utils import *

def avg_layers_with_thermal(rgb, thermal):

    # Split RGB values, not drop of alpha layer
    R,G,B = split_layers_to_3(rgb)
    
    avg_therm = avg_image(thermal)

    # create empty array, populate for new image
    rgbArray = np.zeros((rgb.shape[0],rgb.shape[1],3), 'uint8')
    rgbArray[..., 0] = avg_mat(R, avg_therm)
    rgbArray[..., 1] = avg_mat(G, avg_therm)
    rgbArray[..., 2] = avg_mat(B, avg_therm)

    return rgbArray


def repl_light_with_therm(rgb, thermal, illuminant='D65'):
    '''
    chooses from these illuminants: ['A', 'D50', 'D55', 'D65', 'D75', 'E']
    '''

    # split RGB vals, note: drop of alpha layer
    img_lab = rgb2lab(rgb, illuminant=illuminant)
    avg_therm = avg_image(thermal)

    L,A,B = split_layers_to_3(img_lab)

    # set range to fit in LAB L range (0-100)
    avg_therm_scaled = np.interp(avg_therm, (avg_therm.min(), avg_therm.max()), (0, 100))

    # create empty array, populate for new image
    newLAB = np.zeros((rgb.shape[0],rgb.shape[1],3))
    newLAB[:,:,0] = avg_therm_scaled
    newLAB[:,:,1] = A
    newLAB[:,:,2] = B

    newRGB = lab2rgb(newLAB)

    return img_as_ubyte(newRGB)