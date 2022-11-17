import math

def compute_area_rectangle(height,width):
    area = height * width
    return area

def compute_area_square(value):
    area = compute_area_rectangle(value,value)
    return area

def compute_area_circle(radius):
    area = math.pi * (radius ** 2)
    return area

def compute_area(shape,num_1,num_2=1):
    if shape == 'circle':
        area = math.pi * (num_1 ** 2)
    if shape == 'square':
        area = num_1 ** 2
    if shape == 'rectangle':
        area = num_1 * num_2
    return area

quit = False
while not quit:
    chosen_shape = input('What shape do you have? (\'square\',\'rectangle\',\'circle\',\'quit\') ').lower()
    if chosen_shape == 'square':
        square_length = int(input('What is the length of the square? '))
        squared = compute_area_square(square_length)
        print('Area: ', squared)
    if chosen_shape == 'rectangle':
        rect_height = int(input('What is the height of the rectangle? '))
        rect_width = int(input('What is the width of the rectangle? '))
        rect_area = compute_area_rectangle(rect_height,rect_width)
        print('Area: ', rect_area)
    if chosen_shape == 'circle':
        circ_rad = int(input('What is the radius of the circle? '))
        circ_area = compute_area_circle(circ_rad)
        print('Area: ', circ_area)
    if chosen_shape == 'quit':
        quit = True

# extra = compute_area('rectangle',5,3)
# print(extra)

print('Application closed.')