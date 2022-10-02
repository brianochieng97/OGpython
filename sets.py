# CREATION OF A SET IN PYTHON
# Program to demonstrate the creation of a set
set1 = set()
print("Initial blank set: ")
print(set1)
# creating a set with the use of a string
set1 = set("GeeksForGeeks")
print("\nSet with the use of a string: ")
print(set1)
# creating a set with the use of a constructor(using object to store string)
string = 'GeeksForGeeks'
set1 = set(string)
print("\nSet with the use of an object")
print(set1)
# creating a set with the use of a list
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of a list: ")
print(set1)
# creating a set with a list of numbers(having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of numbers: ")
print(set1)
# creating a set with a mixed type of values(having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of mixed values")
print(set1)
# creating a set with another method(set containing numbers)
my_set = {1, 2, 3}
print(my_set)

# ADDING ELEMENTS TO A SET
# a).using add() method
# creating a set
set1 = set()
print("\nInitial blank set: ")
print(set1)
# Adding element and tuple to the set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after addition of three elements: ")
print(set1)
# adding elements to the set using iterator
for i in range(1, 6):
    set1.add(i)
    print("\nSet after addition of elements from 1-5: ")
    print(set1)
# b).using update () method
# creating a set

# addition of elements to the set using update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after addition of elements using update: ")
print(set1)

# ACCESSING A SET
# creating a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set: ")
print(set1)
# accessing element using for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
# checking the element using in keyword
print("Geeks" in set1)

# REMOVING ELEMENTS FROM THE SET
# a).using remove() method or discard() method
# creating a set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("\nInitial set: ")
print(set1)
# removing elements from a set using remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after removal of elements: ")
print(set1)
# removing elements from a set using discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after discarding two elements: ")
print(set1)
# removing elements from set using iterator method
for i in range(1, 5):
    set1.remove(i)
    print("\nSet after removing a range of elements: ")
    print(set1)