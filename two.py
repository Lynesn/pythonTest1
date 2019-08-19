#Write a Python program to remove and print every second number from a list of numbers until the
#list becomes empty
myList = [1, 2, 34, 12, 77, 66]

for position in range(len(myList)):  # loop through the list
    if len(myList) > 1:              # checks the list length
        removedItem = myList.pop(1)     # removes the second item
print(removedItem)                  # prints the removed item.
