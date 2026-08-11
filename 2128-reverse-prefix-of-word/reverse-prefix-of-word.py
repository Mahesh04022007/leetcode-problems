class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if ch == word[i]:
                return word[:i+1][::-1]+word[i+1:]
        return word 
            

        