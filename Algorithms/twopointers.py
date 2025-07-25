#####################################
# Example Two Pointers Algorithm
# Leetcode 977. Squares of a Sorted Array
#####################################

nums = [-4,-1,0,3,10]

left = 0
rigth = len(nums) - 1
result = []

while left <= rigth:
    if abs(nums[left]) > abs(nums[rigth]):
        result.append(nums[left] ** 2)
        left += 1
    else:
        result.append(nums[rigth] ** 2)
        rigth -= 1

result.reverse()
print(result)