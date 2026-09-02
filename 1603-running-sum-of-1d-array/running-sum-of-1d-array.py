class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        sm=0
        for i in nums:
            sm+=i
            lst.append(sm)
        return lst 

        