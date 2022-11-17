import math

# m = 0 #kg - mass of object
# g = 0 #m/s^2 - acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
# p = 0 #kg/m^3 - density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
# A = 0 #m^2 - cross sectional area of projectile (in square meters)
# C = 0 #drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)
# c = 0.5 * p * A * C
# t = 0 #s - time in seconds

# v = math.sqrt(m * g / c) * (1 - math.exp((0 - math.sqrt(m * g * c) / m) * t))


print('\nWelcome to the velocity calculator. Please enter the following:\n')

m = float(input('Mass (in kg): ')) # for an anvil, input 150
g = float(input('Gravity (in m/s\u00b2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): ')) # ten days & nights would be 864000 seconds
p = float(input('Density of the fluid (in kg/m\u00b3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m\u00b2): ')) # anvil: 0.41
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): ')) # anvil: 0.795

c = 0.5 * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((0 - math.sqrt(m * g * c) / m) * t))
v_terminal = math.sqrt(m * g / c)

print(f'\nThe inner value of c is: {c:.3f}')
print(f'The velocity after {t} seconds is: {v:.3f} m/s')
print(f'The terminal velocity is: {v_terminal:.3f} m/s\n')