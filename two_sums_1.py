class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if (nums[j] == target - nums[i]) and j != i :
                    return [i,j]
            