class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        temp=x
        while x>0:
            r=x%10
            sum+=r
            x//=10
        return sum if temp%sum ==0 else -1
        