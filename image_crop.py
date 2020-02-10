
from PIL import Image
image = Image.open('my1.jpg')
width, height = image.size
area = (200, 200, width/10, height/10)
img = image.crop(area)

#print(image)
#img = image.resize((int(width/4), int(height/4)))
#print(img)

img.save("cropped_picture.jpg")
img.show();