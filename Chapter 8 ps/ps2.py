#Write a python program using function to convert Celsius to Fahrenheit.

# (0°C × 9/5) + 32 = 32°F

n = int(input("Enter the degree number to convert to Fahrenheit: "))

def  convert_celsius_to_fahrenheit(n):
    fahrenheit = (n * 9/5) + 32
    return fahrenheit

print(f"{n}°C to Fahrenheit coversion is : {convert_celsius_to_fahrenheit(n)} F")


