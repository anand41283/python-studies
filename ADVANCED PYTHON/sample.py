a = [1, 2, 3, 5, 4, 3, 3, 5, 5, 67, 8, 8]

# Remove any empty elements if necessary
a = [x for x in a if x]
print(a)

# Create an empty list to store unique elements
unique_elements = []


# Create a corresponding list to store the counts of unique elements
counts = []

# Iterate through each element in the list
for element in a:
    if element in unique_elements:
        # If the element is already in the unique_elements list, increment its count
        index = unique_elements.index(element)
        print(index)
        print(unique_elements)
        counts[index] += 1
    else:
        # If the element is not in the unique_elements list, add it and set its count to 1
        unique_elements.append(element)
        counts.append(1)

# Print the results
for i in range(len(unique_elements)):
    print(f"Element {unique_elements[i]}: {counts[i]} times")
