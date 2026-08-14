class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        sm=0
        n=len(nums)
        for i in nums:
            sm+=i
            prefix.append(sm)
        for i in range(len(nums)):
            leftsum=prefix[i]
            rightsum=prefix[n]-prefix[i+1]
            if leftsum==rightsum:
                return i
        return -1



    
        