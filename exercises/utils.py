import math
import platform

print(math.pi)
x = True
y = True
result = x and y
print(result)

print('Versión kernel :', platform.python_version())

numbers = [1,2,3,4,5]
print(f'{[num ** 2 for num in numbers] = }')