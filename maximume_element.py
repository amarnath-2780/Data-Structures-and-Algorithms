"""
Find the Maximum Element in an Array
Input: [1, 3, 5, 7, 9]
Time complexity :- O(n)
Space Complexity :- O(1)
"""

data = [1, 3, 5, 7, 9]
largest_number = 0

for item in data:
    if item > largest_number:
        largest_number = item 

print("Maximum Element in this array is ", largest_number)
print("Maximum Element in this array is ", max(data))
print("Maximum Element in this array is ", sorted(data)[-1])