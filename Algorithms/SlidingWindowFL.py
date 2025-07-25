#####################################
# Sliding Window Algorithm  
# Fixed Length 
# Leetcode 643. Maximum Average Subarray I
#####################################

nums = [1,12,-5,-6,50,3]
k = 4

n = len(nums)
currentSum = 0

for i in range(k):
    currentSum += nums[i]

maxAverage = currentSum / k

for i in range(k,n):
    currentSum += nums[i]
    currentSum -= nums[i-k]

    average = currentSum / k
    maxAverage = max(maxAverage, average)

print(maxAverage)