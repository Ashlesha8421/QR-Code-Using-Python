#A QR code (short for "quick response" code) is a type of barcode that contains a matrix of dots.
#It can be scanned using a QR scanner or a smartphone with built-in camera.
#Once scanned, software on the device converts the dots within the code into numbers or a string of characters.
#We can also seen image using QR-code
import qrcode

from PIL import Image
img  = qrcode.make("C:\Users\91830\Pictures\QR_Code")
img.save(QR_Image.jpg")