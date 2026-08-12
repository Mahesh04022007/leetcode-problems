class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        sum1=0
        for i in nums:
            sum1+=i
            lst.append(sum1)
        return lst
        