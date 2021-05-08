import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
#Taking input as string
qr=pyqrcode.create("Hello world")#Encoding the message.
qr.png('my_message.png',scale=8)

#Making the output from qrcode
qr_decode=decode(Image.open('my_message.png'))
print(qr_decode[0].data.decode('ascii'))
