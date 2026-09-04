class Solution(object):
    def twoSum(self, nums, target):
        note = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in note:
                return [note[complement],i]
            else :
                note[num] = i