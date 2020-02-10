
from PIL import Image
image = Image.open('my1.jpg')
width, height = image.size
print(image)
img=image.resize((int(width/4), int(height/4)))
print(img)
img.save("resized_image.jpg")
img.show();

