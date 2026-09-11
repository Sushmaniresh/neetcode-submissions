class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        longest = 0 
        numset = set(nums)
        for n in nums:
            if n-1 not in numset:
                length = 1
                while n+length in numset:
                    length+=1
                longest = max(longest,length)
                length=0
        return longest
        