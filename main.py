from PIL import Image as img

file_name = r'C:\Users\gtush\OneDrive\Desktop\GUI\pil\please give me  1.png'
images = img.open(file_name)
images.show()

images = images.resize((int(images.width / 2), int(images.height / 2)), resample=img.LANCZOS, box=(20, 20, 100, 100))
images.show()
