class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        top=max(candies)
        for i in candies:
            if i+extraCandies>=top:
                 out.append(True)
            else:

              
                out.append(False)
        return out
       

        