# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

inputFile = open(r"input.txt", 'r')
input = inputFile.readlines()
l = len(input)
print("length :", l)


for i in range(0,l):
    print('creating qr for :', input[i])
    url = pyqrcode.create(input[i])
    # url.svg("myqr.svg", scale = 8)
    

    url.png(input[i].split('\n')[0] +'.png', scale = 8)
