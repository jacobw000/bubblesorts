# List of items to search through
items = [43,7,6,19,9,15]
length = len(items)-1

# Initialise for loop later
index = 0


# Says how long the list is
print(f"Length of list: {length}")



for x in range (0, length):
    for index in range(0, length):

        # If first item is larger than second, swap
        if (items[index] > items[index+1]):
            num = items[index]
            items[index] = items[index+1]
            items[index+1] = num

print(items)
