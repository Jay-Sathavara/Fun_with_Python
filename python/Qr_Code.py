# JP0030

import pyqrcode
import png
link = "https://github.com/JP0030"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)