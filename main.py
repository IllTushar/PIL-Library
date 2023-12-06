from PIL import Image as img

file_name = r'C:\Users\gtush\OneDrive\Desktop\GUI\pil\please give me  1.png'
images = img.open(file_name)
images = images.rotate(angle=60, expand=True, fillcolor="white", center=(100, 100))
images.show()
