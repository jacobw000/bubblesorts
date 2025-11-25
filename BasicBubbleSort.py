import random
import time

# List of items to search through
y = int(input("Enter list length."))
# Starts a timer
start = time.time()
# Generates a list of 0-100 numbers with y data items 
items = [random.randint(0,100) for x in range(y)]
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

# Ends the timer
end = time.time()
# Makes a variable with the length taken for the search
speed = (end - start)
print(f"Time taken: {speed}")
print(items)


