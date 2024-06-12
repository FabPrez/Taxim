from os import path as osp
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.ndimage import correlate
import scipy.ndimage as ndimage
from scipy import interpolate
import cv2
import argparse

import sys
sys.path.append("..")


## Use this script to resize the gelmap to the size of the secified sensor
## in this case is adapted for the gsmini sensor
## The original gelmap is 480x640 and the new one is 240x320

def modify_gelmap():
    """
    for gelsightm mini sensor"""
    gelpad_model_path = osp.join( '..', 'calibs', 'gelmap5.npy')
    gelmap = np.load(gelpad_model_path)
    # Visualizzare informazioni sull'array
    print("Shape of gelmap:", gelmap.shape)
    print("Type of elements:", gelmap.dtype)
    print("Content preview:", gelmap)
    from scipy.ndimage import zoom

    zoom_factors = (240 / gelmap.shape[0], 320 / gelmap.shape[1])

    gelmap_resized = zoom(gelmap, zoom_factors)

    resized_gel_savePath = osp.join('..', 'calibs','gelmap_gsmini.npy')
    np.save(resized_gel_savePath, gelmap_resized)

    print("Resized shape:", gelmap_resized.shape)

    return gelmap_resized

def flat_gelmap():
    gelpad_model_path = osp.join( '..', 'calibs', 'gelmap_gsmini.npy')
    gelmap = np.load(gelpad_model_path)
    mean_value = np.mean(gelmap)
    gelmap[:] = mean_value
    
    resized_gel_savePath = osp.join('..', 'calibs','gelmap_gsmini_flat.npy')
    np.save(resized_gel_savePath, gelmap)

    return gelmap
    
    
if __name__ == "__main__":
    flat_gelmap()
    
