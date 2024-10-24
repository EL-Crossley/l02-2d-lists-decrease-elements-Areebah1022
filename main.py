# Put your function here
decreaseElements(lists):
    return [[element - 1 for element in row] for row in lists]

# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(decreaseElements(nums))
