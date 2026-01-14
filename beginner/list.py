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

ranges=list(range(1, 11))
print("Numbers from 1 to 10:", ranges)
new_ranges=range(5)
print("Numbers from 0 to 4:", list(new_ranges))

immutable_tuple=(1, 2, 3)
# immutable_tuple[0] = 10  # This will raise a TypeError
print("Tuple contents:", immutable_tuple)
# imutable_tuple.append(4)  # This will raise an AttributeError