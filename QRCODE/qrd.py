import qrcode
import png
img=qrcode.make("https://www.youtube.com/watch?v=-GmJLI122ZM")
img.save("k.jpg")
img=qrcode.make("hello")
img.sav("l.jpg")