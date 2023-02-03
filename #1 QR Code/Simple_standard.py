# //Simple and standard qr code

import qrcode as qr
img=qr.make("https://www.google.com/");
img.save("google.png");