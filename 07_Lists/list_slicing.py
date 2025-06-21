# List slicing examples

nums = [10, 20, 30, 40, 50, 60, 70]

print("Original list:", nums)
print("First 3 elements:", nums[:3])
print("Middle elements (index 2 to 5):", nums[2:6])
print("Last 3 elements:", nums[-3:])
print("Every second element:", nums[::2])
print("Reversed list:", nums[::-1])



# output:
# Original list: [10, 20, 30, 40, 50, 60, 70]
# First 3 elements: [10, 20, 30]
# Middle elements (index 2 to 5): [30, 40, 50, 60]
# Last 3 elements: [50, 60, 70]
# Every second element: [10, 30, 50, 70]
# Reversed list: [70, 60, 50, 40, 30, 20, 10]
