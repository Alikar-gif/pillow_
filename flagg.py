from PIL import Image, ImageOps, ImageDraw

Blue = (0,106,167)
Yellow = (524,204,0)

im = Image.new("RGB",(160,100),Yellow)

Img = ImageDraw.Draw(im)

Img.rectangle([(50, 0), (70, 100)], Blue)
Img.rectangle([(0, 40), (160, 60)], Blue)

im.save("egirevs.png")