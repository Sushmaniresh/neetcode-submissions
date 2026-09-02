class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in nums:
            rob1, rob2 = max(rob2+n, rob1), rob1
        return rob1
        