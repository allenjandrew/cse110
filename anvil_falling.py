import math

time = 864000 # 10 days and nights falling...
m = 150 # an average anvil weighs 150 kg.
g = 9.8 # gravity of earth (m/s^2). I'm assuming it's the same for heaven and tartarus.
p = 1.3 # density of air (kg/m^3).
A = .41 # cross sectional area of anvil (m^2).. I looked this up, though it might not be 100% accurate.
C = .795 # drag constant for an anvil I looked this up as well.

c = 0.5 * p * A * C
velocity = math.sqrt(m * g / c) * (1 - math.exp((0 - math.sqrt(m * g * c) / m) * time))
v_terminal = math.sqrt(m * g / c)

print(f'\nTerminal velocity: {v_terminal} m/s') # This prints out the terminal velocity of the anvil.

# It turns out that this anvil will reach its terminal velocity at around one minute.
# So, my next equation multiplies the velocity by the time minus one minute, plus the average velocity of the first minute.
# This is approximate, but close. 

distance = velocity * (time - 30)

print(f'\nDistance in meters: {distance:.3f} m')
distance_km = distance / 1000
print(f'\nDistance in kilometers: {distance_km:.3f} km')
distance_mi = distance / 1609.344
print(f'\nDistance in miles: {distance_mi:.3f} mi')
wowza = math.floor(distance_mi)
print(f'\nThe distance between Olympus and earth, and between earth and Tartarus, is over {wowza} miles!\n')