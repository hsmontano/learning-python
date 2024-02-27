import math
print("***In this program we are going to calculate the area of a shape***")

hight = float(input("Input the hight value: "))
width = float(input("Input the width value: "))

print("The area of rectangle is: ", hight * width)
print("The perimetro of rectangle is: ", 2 * (hight + width))

radio = float(input("Input the radio value: "))

print("The area of circle is: ", math.pi*radio**2)
print("The perimetro of circle is: ", 2 * math.pi * radio)