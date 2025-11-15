from PIL import Image

img = Image.open("logo.png")
img.convert("RGB").save("logo.jpg")