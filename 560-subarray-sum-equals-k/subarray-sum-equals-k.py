class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix +hashmap solution
        csum=0#this is our prefix sum
        subcnt=0#how many subarrays have we seen with sum k
        seen={0: 1}#hashmap to store prefix sums found so far
        for i in nums:
            #compute prefix sum
            csum+=i
            #required prefix sum (prefix(l-1),history)

            req=csum-k
            #check if req in seen prefixes so far
            if req in seen :
                subcnt+=seen[req]#add the number of time we seen that prefix
            #Push the current prefix in hashmap
            seen[csum]=seen.get(csum,0)+1
        return subcnt




        