names=['Alice', 'Bob', 'Charlie', 'Diana']
print("First name:", names[0])
for name in names:
    print(f'Hello, {name}!')

numbers=[10, 20, 30, 40, 50]
total=sum(numbers)
print("Total sum:", total)
numbers.append(60)
print("Updated numbers:", numbers)
numbers.insert(0, 5)
print("After inserting 5 at the beginning:", numbers)
numbers.remove(30)
print("After removing 30:", numbers)
print(10 in numbers)