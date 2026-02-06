# https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()

        count = 0
        idx = 0
        for i in range(n):
            while nums[idx]*k < nums[i]:
                idx += 1
            count = max(count, i-idx+1)

        return n - count