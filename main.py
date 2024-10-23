# Put your function here
decreaseElements(n):
    return [[element - 1 for element in row] for row in n]

# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(decreaseElements(nums))
