#!/usr/bin/env python3
import numpy as np
import lab4_utils
import cv2 as cv

from matplotlib import pyplot as plt
from PIL import Image


# 0. Image data
data = lab4_utils.create_rainbow()
plt.imshow(data)
plt.show()

# 1. Convert RGB to YCbCr
ycbcr_matrix = np.array(
    [[.229, .587, .114], [-.168, -.331, .5], [.5, -.418, -.082]])
a = np.clip(np.dot(data, ycbcr_matrix), a_min=0, a_max=255)
plt.imshow(a.astype(np.uint8))
plt.show()

# 2. Downsampling on Cb Cr
# TODO: implement

# 3. Produce 8x8 blocks
# TODO: implement

# 4. Calculate DCT on each block
# TODO: implement

# 5. Divide each block by quantisation matrix
# TODO: implement

# 6. Round each block to integers
# TODO: implement

# 7. Zig Zag
# TODO: implement

# 8. Flatten, concatenate, compress and calculate the size -- how many bytes?
# TODO: implement

# 7'. Undo Zig Zag
# We can skip it in this exercise!

# 6'. Nothing to do here   ¯\_(ツ)_/¯
# For the next step, just reuse the rounded data obtained in step 6.

# 5'. Reverse division by quantisation matrix -- multiply
# TODO: implement

# 4'. Reverse DCT
# TODO: implement

# 3'. Combine 8x8 blocks to original image
# TODO: implement

# 2'. Upsampling on Cb Cr
# TODO: implement

# 1'. Convert YCbCr to RGB
# TODO: implement

# 0'. Save the decoded image -- as PPM or PNG
# TODO: implement
