import cv2
import os

def encrypt(msg):
    img = cv2.imread("joyboy.jpg")  # Replace with the correct image path
    password = input("Enter a passcode:")

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg") # Use 'start' to open the image on Windows
    return img, password


