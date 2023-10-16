import cv2
import numpy as np

imagem = cv2.imread("img.jpg")

imagem_normalizada = imagem / 255.0

alpha = 300

imagem_com_contraste = cv2.convertScaleAbs(imagem_normalizada, alpha=alpha, beta=0)

imagem_reducao_ruido = cv2.medianBlur(imagem_com_contraste, 3)

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Tratada", imagem_com_contraste)
cv2.imshow("Imagem Sem Ruído", imagem_reducao_ruido)
cv2.waitKey(0)