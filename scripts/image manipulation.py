from PIL import Image
a = Image.open('start.jpg')
b = a.resize((210, 210)).save('start.gif')