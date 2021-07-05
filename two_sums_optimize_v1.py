 # create a dict with keys are values of List and values are indexes of List
class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}        #create Dict        
        for i in nums:
           res[i] = nums.index(i)   
        for j in range(len(nums)):
           sub = target - nums[j]
           if sub in res and j != res[sub]: #check if "sub" in "res" => return res[sub] (value of Dict) is one of idexes of List
              return [j,res[sub]]
