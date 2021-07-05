class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in nums:
           res[i] = nums.index(i)
        for j in range(len(nums)):
           sub = target - nums[j]
           if sub in res and j != res[sub]:
              return [j,res[sub]]
