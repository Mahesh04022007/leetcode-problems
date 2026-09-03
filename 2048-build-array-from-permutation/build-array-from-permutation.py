class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(len(nums)):
            out.append(nums[nums[i]])
        return out
        