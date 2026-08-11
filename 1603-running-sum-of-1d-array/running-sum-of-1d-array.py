class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        out =[]
        for i in nums:
            s+=i
            out.append(s)
        return out
        