#Quick_Response code
#A QR code (short for "quick response" code) is a type of barcode that contains a matrix of dots.
#It can be scanned using a QR scanner or a smartphone with built-in camera.
#Once scanned, software on the device converts the dots within the code into numbers or a string of characters.

import pyqrcode
import png

def qr_code():
    s='Welcome to qr_code_generator using python'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=6)
    print('Code Executed properly')

if __name__ == '__main__':
    qr_code()
