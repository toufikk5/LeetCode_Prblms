class Solution(object):
    def lengthOfLongestSubstring(self, s):
       save = set()
       left = 0
       max_length =0
       
       for right,char in enumerate(s):
          while char in save:
            save.remove(s[left])
            left+=1

          save.add(char)
          max_length = max(max_length,right-left+1)
       return max_length
        