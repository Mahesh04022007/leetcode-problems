class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst=[]
        for i in accounts:
            sm=0
            for va in i:
                sm+=va
            lst.append(sm)
        return max(lst)

        