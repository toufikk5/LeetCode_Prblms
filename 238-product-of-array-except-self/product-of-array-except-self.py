class Solution(object):
    def productExceptSelf(self, nums):
        n =len(nums)
        left_pr=[1]*n
        right_pr = [1]*n
        answer = []

        for i in range(1,n):
            left_pr[i]=left_pr[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            right_pr[i] = right_pr[i+1]*nums[i+1]

        for i in range (n):
            answer.append(left_pr[i]*right_pr[i])
        return answer



       
        