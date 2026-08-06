class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        firstwindow=arr[:k]
        currentsum=sum(firstwindow)
        count=0
        if currentsum/k >=threshold:
            count+=1
        for i in range(k,len(arr)):
            #adding new elements to currentsum
            #subtracting old element (left most element in window)
            currentsum=currentsum+arr[i]-arr[i-k]
            if currentsum/k>=threshold:
                count+=1
        return count

        