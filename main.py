from PIL import Image, ImageOps

Thim_ = Image.open("Thim.jpeg")
Thim_ = ImageOps.flip(Thim_)

Thim_.save("new_thim.jpg")

