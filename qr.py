import pyqrcode
import png
from pyqrcode import QRCode
s = input('enter the url of website:')
url = pyqrcode.create(s)
url.svg("myqr.svg",scale = 8)
url.png("myqr.png",scale = 8)
