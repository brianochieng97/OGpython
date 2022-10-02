# ADDING ELEMENTS TO PYTHON LIST
# USING APPEND () METHOD
# python program to demonstrate addition of elements in a list
List = []
print("Initial blank lists: ")
print(list)
# addition of the elements in the list
List.append(1)
List.append(2)
List.append(4)
print("\nList after addition of three elements")
print(List)
# Adding elements to the list using Iterator
for i in range(1, 4):
    List.append(i)
    print("\nList after addition of elements from 1-3: ")
    print(List)
# Adding tuples to the list
List.append((5, 6))
print("\nList after addition of a tuple: ")
print(List)
# addition of list to a list
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after addition of a list: ")
print(List)

# USING INSERT () METHOD
# Python program to demonstrate addition of elements in a list
List = [1, 2, 3, 4]
print("\nInitial list: ")
print(List)
# addition of elements at specific position using insert method
List.insert(3, 12)
List.insert(0, 'Greek')
print("\nList after performing Insert operation: ")
print(List)

# USING EXTEND () METHOD
# Python program to demonstrate addition of elements in a list
List = [1, 2, 3, 4]
print("\nInitial List: ")
print(List)
# addition of multiple elements to the list at the end
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing extend operation: ")
print(List)

# REVERSING  LIST
# USING REMOVE () METHOD