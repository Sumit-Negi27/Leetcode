class Solution(object):
    def twoSum(self, nums, target):
      l=[]  
      for i in range(len(nums)):
        for j in range(1,len(nums),1):
            if i!=j:
                if nums[i]+nums[j]==target:
                    return i,j
