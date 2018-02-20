import numpy as np
import cv2


rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imwrite("bitwise_rectangle.png", rectangle)


circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imwrite("bitwise_circle.png", circle)


bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imwrite("bitwise_and.png", bitwiseAnd)

bitwiseNAnd = cv2.bitwise_not(bitwiseAnd)
cv2.imwrite("bitwise_nand.png", bitwiseNAnd)

bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imwrite("bitwise_or.png", bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imwrite("bitwise_xor.png", bitwiseXOR)


bitwiseNOR = cv2.bitwise_and(cv2.bitwise_not(rectangle), cv2.bitwise_not(circle))
cv2.imwrite("bitwise_nor.png", bitwiseNOR)


bitwiseXNOR = cv2.bitwise_or(bitwiseAnd, bitwiseNOR)
cv2.imwrite("bitwise_xnor.png", bitwiseXNOR)

bitwiseNOT = cv2.bitwise_not(circle)
cv2.imwrite("bitwise_not_circle.png", bitwiseNOT)
