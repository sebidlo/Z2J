# 6.3 Challenge: Convert Temperatures

def convert_cel_to_far(c):
    f = c * 9/5 + 32
    print(f"{f:.2f} degrees F = {c} degrees C")

degrees_c = float(input("Enter a temperature in degrees C:"))
convert_cel_to_far(degrees_c)

def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    print(f"{f} degress F = {c:.2f} degrees C")

degrees_f = float(input("Enter a temperature in degrees F:"))
convert_far_to_cel(degrees_f)

