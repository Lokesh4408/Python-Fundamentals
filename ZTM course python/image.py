from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
# filtered_img = img.filter(ImageFilter.GaussianBlur) # BLUR
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.png', 'png')

print(img.format)
print(img.size)
print(img.mode)
# print(dir(img))
filtered_img.save('filtered_img.png') # filtered_img.resize((300,300)), filtered_img.rotate
# filtered_img.show()

new_img = Image.open('./astro.jpg')
# new_img = new_img.resize((400, 400)) # to keep the aspect ration we can use thumbnail instead of resize method.
new_img.thumbnail((400, 400))
new_img.save('thumbnail.jpg')