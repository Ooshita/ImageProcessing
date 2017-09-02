import numpy as np
import cv2

img = cv2.imread('./lena.jpg')
# 画像をただ表示するだけ
cv2.imshow('image',img)
# ０が入力されたら終了．それまで待機
cv2.waitKey(0)
cv2.destroyAllWindows()
