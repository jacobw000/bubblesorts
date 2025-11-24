# List of items to search through
import random
import time


y = int(input("Enter list length."))
start = time.time()
items = [random.randint(0,100) for x in range(y)]
length = len(items)-1

# Initialise for loop later
swapped = True

# If a swap has happened, do a pass
while (swapped) and length > 0:

    swapped = False

    for index in range(0, length):

        # If first item is larger than second, swap
        if (items[index] > items[index+1]):
            
            num = items[index]
            items[index] = items[index+1]
            items[index+1] = num

            # Tells the code that a swap did happen, and another one will need to
            swapped = True
    length = length - 1
 
end = time.time()
speed = (end - start)
print(f"Time taken: {speed}")
print(items)
