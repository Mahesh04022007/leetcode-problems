class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxw=0
        for i in accounts:
            s=0
            for value in i:
                s+=value
            if s>maxw:
                maxw=s
        return maxw
        

        