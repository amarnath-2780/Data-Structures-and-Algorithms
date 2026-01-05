

data = [10, 5, 12, 3, 7]

minimum_element = float('inf')

for item in data:
    if item < minimum_element:
        minimum_element = item 

print("Maximum Element in this array is ", minimum_element)
print("Maximum Element in this array is ", min(data))
print("Maximum Element in this array is ", sorted(data)[0])
