import sys
from PIL import Image
image_name = sys.argv[1]
image = Image.open(image_name)
gray = image.convert("L")
gray.save(image_name)
