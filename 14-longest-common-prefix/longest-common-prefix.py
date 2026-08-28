class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            j = 0

            while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
                j += 1

            prefix = prefix[:j]

            if prefix == "":
                return ""

        return prefix
        
       

        
    
    