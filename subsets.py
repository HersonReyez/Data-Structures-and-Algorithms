#####################################
# Recursive Backtracking 
# LeetCode - 78. Subsets
#####################################

nums = [1,2,3]

n = len(nums)
res, sol = [], []

def backtrack(i):
    if i == n:
        # Add a copy of current sol
        res.append(sol[:]) 
        return
    
    # Don't pick nums[i]
    backtrack(i+1)

    # Pick nums[i]
    sol.append(nums[i])
    backtrack(i+1)
    sol.pop()

backtrack(0)

print(res)