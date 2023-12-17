numbers = []
numbers.append(5)
numbers.append(8)
numbers.extend([6, 7, 8])
del numbers[1]
numbers.insert(3, 30)

print(numbers)
print(len(numbers))

