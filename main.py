import cv2
import numpy as np

imagem = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

valor_limiar = 100

_, imagem_limiarizada = cv2.threshold(imagem, valor_limiar, 255, cv2.THRESH_BINARY)

#(b, g, r) = cv2.split(imagem)

#cv2.imshow("Imagem Azul", b)
#cv2.imshow("Imagem Verde", g)
#cv2.imshow("Imagem Vermelha", r)



cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Limiarizada", imagem_limiarizada)
cv2.waitKey(0)