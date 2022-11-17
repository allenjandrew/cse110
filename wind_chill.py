print()

def convert_temp(degrees,convert_to_celsius=False):
    if not convert_to_celsius:
        new_temp = (degrees * 9 / 5) + 32
    elif convert_to_celsius:
        new_temp = (degrees - 32) * 5 / 9
    return new_temp

def get_wind_chill(degrees,wind_velocity):
    wind_chill = 35.74 + (0.6215 * degrees) - (35.75 * (wind_velocity ** 0.16)) + (0.4275 * degrees * (wind_velocity ** 0.16))
    return wind_chill


f_temp = int(input('What is the temperature? '))
degree_format = input('Fahrenheit or Celsius (F/C)? ').upper()
print()

if degree_format == 'C':
    c_temp = f_temp
    f_temp = convert_temp(c_temp)
    print(f'{c_temp}˚C is equal to {f_temp:.2f}˚F.')

wind_v = 5
while wind_v <= 60:
    wind_chill = get_wind_chill(f_temp,wind_v)
    if degree_format == 'C':
        wind_chill = convert_temp(wind_chill,convert_to_celsius=True)
    print(f'At wind speed of {wind_v} mph, windchill is {wind_chill:.2f}˚{degree_format}.')
    wind_v += 5

print()