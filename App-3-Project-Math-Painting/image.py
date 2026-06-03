"""
this is a test file
"""

import numpy as np
from PIL import Image

data = np.zeros((500, 400, 3), dtype=np.uint8)
data[:] = [255, 255, 0] # generates the cube of these dimensions made up of zeroes
print(data)

# data[1:3] = [255,0,0] # index first and second row turns red
# data[:, 1:3] = [255,0,0] # index first and second column turns red
# data[1:3, 1:3] = [255,0,0] # index first and second row and column turns red


img = Image.fromarray(data, 'RGB')
img.save("canvas.png")

# import os
# print(os.path.exists("canvas.png"))
# print(os.getcwd())