import qrcode as qr
#from PIL import Image
img = qr.make("https://github.com/gunna-rahul")
img.save("gunnarahul_github.png")
