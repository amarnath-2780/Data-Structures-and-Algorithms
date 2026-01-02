
def twoSum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  hash = {}
  for index,value in enumerate(nums):
      hash[value] = index
  
  for i in range(len(nums)):
      if  (target - nums[i]) in hash and hash[target - nums[i]] != i:
          return [hash[target-nums[i]], i]
        
