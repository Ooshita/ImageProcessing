# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('./lena.jpg')
    # 画像サイズの取得（横，縦）
    size = tuple(np.array([img.shape[1], img.shape[0]]))

    rad = np.pi / 4 # 45度回転（π/4）
    # x軸方向に平行移動させたい距離
    move_x = 0
    # y軸方向に平行移動させたい距離
    move_y = img.shape[0] * -0.5

    matrix = [
                [np.cos(rad), -1*np.sin(rad), move_x],
                [np.sin(rad), np.cos(rad), move_y]
             ]
    affine_matrix = np.float32(matrix)
    image_affine = cv2.warpAffine(img, affine_matrix, size, flags=cv2.INTER_LINEAR)

    # 表示
    plt.imshow(image_affine, cmap='gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()
