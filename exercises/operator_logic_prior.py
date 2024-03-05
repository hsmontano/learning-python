m = True
l = False
n = True
print("n is type: ", type(n), "and its value is: ", n)

numbers=dict()
lista = [[1, "uno", "True", "1.0"], [2, "dos", "True", "2.0"], [3, "tres", "True", "3.0"], [3, "tres", "True", "3.0"]]

def add(num):
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1

for l in lista:
    add(l[0])

print(numbers)