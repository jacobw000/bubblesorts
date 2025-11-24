# List of items to search through
items = [43,7,6,19,9,15]
length = len(items)-1

# Initialise for loop later
index = 0
swapped = True

# If a swap has happened, do a pass
while (swapped):

    swapped = False

    for index in range(0, length):

        # If first item is larger than second, swap
        if (items[index] > items[index+1]):
            
            num = items[index]
            items[index] = items[index+1]
            items[index+1] = num

            # Tells the code that a swap did happen, and another one will need to
            swapped = True

print(items)
