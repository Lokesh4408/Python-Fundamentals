import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if folder/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# loop through images folder and convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(clean_name)
    print('all done!')
# save to a new folder