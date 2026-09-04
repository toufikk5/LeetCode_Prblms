class Solution(object):
    def singleNumber(self, nums):
       note = {}
    
       for nbr in nums:
         if nbr not in note:
            note[nbr] = 1
         else :
            note[nbr] +=1
        
       for key , value in note.items():
            if value == 1 :
                return key

       
        