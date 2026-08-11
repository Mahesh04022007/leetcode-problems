class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        n=x
        
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        if x==rev:
            return True
        else:
            return False
        