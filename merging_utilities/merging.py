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