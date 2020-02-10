#installed in cmd pip install pillow
from PIL import Image

image=Image.open('my1.jpg')
image.show()

#transposing image
transposed_img = image.transpose(Image.FLIP_LEFT_RIGHT)
#saving transposed image
transposed_img.save("transposed1.jpg")
transposed_img.show()


