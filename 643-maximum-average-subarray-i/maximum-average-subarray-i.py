class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


    #slidingwindow(fixed length)
        maxaverage=-10000000
        left=0
        right=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right>=k-1:
                avg=currentsum/k
                maxaverage=max(avg,maxaverage)
            #subtracting the valueon left 
                currentsum-=nums[left]
                left+=1
        return maxaverage
        

                       
    