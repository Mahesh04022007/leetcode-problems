class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        open="{[("
        close="}])"
        for i in s:
            if i in open:#open brackers goes into stack
                st.append(i)
            else:                        #when closed bracket is encountered
                            #if stack is empty,sequence is invalid
                if not st:
                    return False
                else:# check  if stack top is corresponding open bracket for this close
                    if i==")"and st[-1]=="(" or i=="]" and st[-1]=="[" or  i=="}" and st[-1]=="{":

                        st.pop()
                    else:
                        return False
        return not st

                    


        