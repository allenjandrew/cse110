from PIL import Image
import random

backgrounds = 'beach','desert','earth','field','forest','snowscape','sunset'
chosen_b = random.choice(backgrounds)
fronts = 'boat','cactus','cat_small','cat','harvester','hiker','penguin','spaceshuttle'
chosen_f = random.choice(fronts)
image_background = Image.open(f'{chosen_b}.jpg')
image_front = Image.open(f'{chosen_f}.jpg')
# image_background.show()
# image_front.show()

width, height = image_background.size
pixels_b = image_background.load()
pixels_f = image_front.load()

# This code was for the milestone, but it's unnecessary in the final result.
# z = 0
# while z < 5:
#     x = random.randint(10,width-10)
#     y = random.randint(10,height-10)
#     r, g, b = pixels_original[x,y]
#     print(f'point ({x}, {y})')
#     print(f'rgb = ({r}, {g}, {b})')
#     for numx in {x-2,x-1,x,x+1,x+2}: # I added these for loops to change more pixels at a time so they're easier to see!
#         for numy in {y-2,y-1,y,y+1,y+2}:
#             pixels_original[numx,numy] = (255,0,255)
#     z += 1
# image_original.show()

# checks to find the value of a specific pixel
# r,g,b = pixels_f[10,10]
# print(f'{r}, {g}, {b}')
# r,g,b = pixels_f[328,307]
# print(f'{r}, {g}, {b}')

image_new = Image.new("RGB",[width,height])
pixels_new = image_new.load()

for i in range(width):
    for j in range(height):
        r,g,b = pixels_f[i,j]
        if r < 150 and g > 180 and b < 150 and (abs(r-b) < 50 or g > r + b):
            pixels_new[i,j] = pixels_b[i,j]
        else:
            pixels_new[i,j] = pixels_f[i,j]

image_new.show()