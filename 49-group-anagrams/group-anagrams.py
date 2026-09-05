class Solution(object):
    def groupAnagrams(self, strs):
        grps ={}
        for word in strs :
            key = "".join(sorted(word))
            if key not in grps:
                grps[key] = [word]
            else :
                grps[key].append(word)
        return list(grps.values())



        