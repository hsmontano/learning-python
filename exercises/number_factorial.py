factorial = 1
i = 1
facts = []
n = int(input("Input value to calculate factorial: "))

while i <= n:
    factorial = factorial * i
    i += 1
    facts.append(factorial)

print(facts)

a=1245
print(a.is_integer())