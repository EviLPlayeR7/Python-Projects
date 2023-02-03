# designing own qr code style

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=5,);
qr.add_data("https://www.google.com");
qr.make(fit=True)
img = qr.make_image(fill_color="pink",back_color="black");
img.save("googlee.png");