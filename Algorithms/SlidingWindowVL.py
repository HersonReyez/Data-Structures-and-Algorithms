#####################################
# Sliding Window Algorithm  
# Variable Length 
# LeetCode - 3. Longest Substring Without Repeating Characters 
#####################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        chars = set()
        n = len(s)

        for right in range(n):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
        
            size = (right - left) + 1
            longest = max(longest, size)
            chars.add(s[right])

        return longest