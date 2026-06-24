
print(f"{i}" for i in range(5)) # This will print a generator object, not the numbers from 0 to 4.

# To print the numbers from 0 to 4, you can use a list comprehension or simply convert the generator to a list:
print([f"{i}" for i in range(5)]) # This will print the list