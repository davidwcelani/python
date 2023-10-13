import cv2
import numpy as np

imagem = cv2.imread("img.jpg")

#imagem[170:180, 70:80] = (255, 255, 255)
print(imagem[175][75])


cv2.imshow("Imagem", imagem)
cv2.waitKey(0)