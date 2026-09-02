class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
     
        mx=0
        for i in sentences:
            words=i.split()
            x=len(words)
            if x>mx:
                mx=x
        return mx