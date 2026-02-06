# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        mpp = {}

        for i in range(n):
            need = target - nums[i]
            if need in mpp:
                return [mpp[need], i]
            mpp[nums[i]] = i

        return []