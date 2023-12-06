'''
Image processing library=>
OpenCv, PIL , PILLOW
'''
from PIL import Image as img

file_name = r'C:\Users\gtush\OneDrive\Desktop\GUI\pil\icons8-dice-32.png'

try:
    images = img.open(file_name)
    images.show()
except Exception as e:
    print(f"An error occurred: {e}")
