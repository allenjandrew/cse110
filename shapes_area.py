import math
sq_l = float(input('\nSquare length (cm): '))
sq_a = sq_l ** 2
sq_m2 = sq_a / 10000
print(f'Square area: {sq_a}cm\u00b2 or {sq_m2}m\u00b2')
re_l = float(input('\nRectangle length (cm): '))
re_w = float(input('Rectangle width (cm): '))
re_a = re_l * re_w
re_m2 = re_a / 10000
print(f'Rectangle area: {re_a}cm\u00b2 or {re_m2}m\u00b2')
ci_r = float(input('\nCircle radius (cm): '))
ci_r2 = ci_r ** 2
ci_a = ci_r2 * math.pi
ci_r2_m2 = ci_r2 / 10000
ci_a_m2 = ci_a / 10000
print(f'Circle area: {ci_r2}\u03C0cm\u00b2 ({ci_r2_m2}\u03C0m\u00b2) or {ci_a}cm\u00b2 ({ci_a_m2}m\u00b2)\n')

number = float (input('Number Fun - give me a number!\n'))
print(f'Area of a square with that side length: {number ** 2}')
print(f'Volume of a cube with that side length: {number ** 3}')
print(f'Area of a circle with that radius: {number ** 2}\u03C0 or {(number ** 2) * math.pi}')
print(f'Volume of a sphere with that radius: {(number ** 3) * (4 / 3)}\u03C0 or {((number ** 3) * math.pi) * (4 / 3)}')
print('')