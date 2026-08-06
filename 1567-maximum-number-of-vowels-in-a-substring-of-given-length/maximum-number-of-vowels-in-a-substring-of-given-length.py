class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        firstwindow=s[:k]
        vowels="aeiou"
        count=0
        for i in firstwindow:
            if i in vowels:
                count+=1
        maxcount=count
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1
            maxcount=max(count,maxcount)   
        return maxcount   
        
        