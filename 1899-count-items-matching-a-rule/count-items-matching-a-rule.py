class Solution:
    def countMatches(self, items: List[List[str]], rulekey: str, rulevalue: str) -> int:
        count=0
        for i in items:
            typ=i[0]
            colour=i[1]
            name=i[2]
            if rulekey=="type":
                if typ==rulevalue:
                    count+=1
            elif rulekey=="color":
                if colour==rulevalue:
                    count+=1
            else:
                if name==rulevalue:
                    count+=1
        return count
           

        