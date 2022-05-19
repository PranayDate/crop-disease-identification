

import os

from shutil import copyfile
import scipy.misc
import matplotlib
import imageio

folder_path = "test"

dst_folder_path = "test-detect"

images_path = os.listdir(folder_path)
index = 0

jpg_files = []
dest_files = []

for n, image in enumerate(images_path):
    src = os.path.join(folder_path, image)
    jpg_files.append(src)
    src1 = os.path.join(dst_folder_path, image)
    dest_files.append(src1)

for index in range(0, len(jpg_files)):
    I1 = imageio.imread(jpg_files[index], pilmode='RGB')
    I3 = I1
    I2 = matplotlib.colors.rgb_to_hsv(I1)
    x1, y1, z = I1.shape
    for y in range(0, y1):
        for x in range(0, x1):

            color = I2[y][x]
            # print(color)
            if (color[0] >= 0.05 and color[0] <= 0.20):
                # print('1')
                I3[y][x][0] = 128
                I3[y][x][1] = 128
                I3[y][x][2] = 0
            elif (color[0] >= 0.2 and color[0] <= 0.41):
                # print('3')
                I3[y][x][0] = 0
                I3[y][x][1] = 255
                I3[y][x][2] = 0
            else:
                I3[y][x][0] = 0
                I3[y][x][1] = 0
                I3[y][x][2] = 0

    # I3 = scipy.misc.imrotate(I3, 180)

    from skimage.io import imsave

    imsave(dest_files[index], I3)
    # scipy.misc.imsave(dest_files[index], I3, 'jpeg')
    print(index)
    #break