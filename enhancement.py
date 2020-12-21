from PIL import Image
import itertools

# open image
image = Image.open("unnamed.jpg")  # you have to pass the input image path as input arg
image = image.convert("L")  # convert to signle channeled image

row, cal = image.size
totalPixels = row * cal

freq = [0] * 256  # fill
cProbability = [0] * 256  # fill zeros

# save original image histogram
freq = image.histogram()

# HISTOGRAM EQUALIZATION
prevSum = 0
for i in range(256):
    prevSum += freq[i] * 1.0 / totalPixels  # add the probablity to calculate
    cProbability[i] = prevSum


pixels = image.load()  # allows the image to be writable
for x, y in itertools.product(range(row), range(cal)):
    pixels[x, y] = int((255 * cProbability[pixels[x, y]]))  # (L-1) * cummulative probability
print(freq)
print(cProbability)
# save resultant image and histogram
image.save('u.jpg')
