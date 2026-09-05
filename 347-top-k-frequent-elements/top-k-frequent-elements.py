class Solution(object):
    def topKFrequent(self, nums, k):
      dict_n ={}
      for nbr in nums:
        if nbr not in dict_n:
            dict_n[nbr] = 1
        else:
            dict_n[nbr] +=1
            
      sorted_items = sorted(dict_n.items(),key = lambda item:item[1],reverse=True)

      result=[]
      for p in sorted_items[:k]:
        result.append(p[0])
      return result


