# Given an array of ints, return a 
# new array length 2 containing the first
#  and last elements from the original 
# array. The original array will be length 
# 1 or more.
def make_ends(things):
    return [things[0], things[-1]]

print(make_ends([1, 2, 3])) # [1, 3])
print(make_ends([1, 2, 3, 4])) # [1, 4])
print(make_ends([7, 4, 6, 2])) # [7, 2])