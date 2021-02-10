
import qrcode
from PIL import Image
import cv2
import webbrowser

img = qrcode.make("https://github.com/RahulMukthineni")
img.save("qr.jpg")



d = cv2.QRCodeDetector()
retval, points, straight_qrcode	=d.detectAndDecode(cv2.imread("qr.jpg"))
print(retval)


webbrowser.open(retval, new=2)