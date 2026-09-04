class Solution(object):
    def containsDuplicate(self, nums):
        note = {}
        for i,nbr in enumerate(nums) :
            if nbr in note:
                return True
            else:
                note[nbr] = i
        return False
    

        