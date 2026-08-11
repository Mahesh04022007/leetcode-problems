def get_sum(n):
    dsum=0
    while n>0:
        r=n%10
        dsum+=r
        n=n//10
    return dsum

class Solution:
    def addDigits(self, n: int) -> int:
        while True:
            if n<10:
                break
            n=get_sum(n)
        return n        