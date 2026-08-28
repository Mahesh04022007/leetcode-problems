class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        if  x==len(set(nums)):
            return False
        else:
            return True

        