import qrcode

website = "httpS://www.innovationyourself.com/"

filename="site.png"

img=qrcode.make(website)
img.save(filename)
