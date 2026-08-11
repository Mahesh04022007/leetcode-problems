class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        nums.sort()
    
        for i in range(len(nums)):
             left,right=i+1,len(nums)-1
             while left<right:

                triplet=(nums[i],nums[left],nums[right])
                sm=sum(triplet)
                if sm>0:
                    right-=1
                elif sm<0:

                    left+=1
                else:
                
                    result.add(triplet)
                    left+=1
                    right-=1
        
       
        return list(result)
        