class Solution(object):
    def isAnagram(self, s, t):
        dict_s = {}
        if len(s) != len(t):
            return False
        
        i=1
        for char in s :
            if char not in dict_s:
                dict_s[char] = i
            else:
                dict_s[char] += 1
        
        for char in t:
            if char not in dict_s:
                return False
            else:
                dict_s[char]-=1

        return all(count == 0 for count in dict_s.values())
    
        