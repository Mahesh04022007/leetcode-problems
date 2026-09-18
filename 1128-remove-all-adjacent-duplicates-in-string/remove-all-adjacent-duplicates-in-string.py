class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in s:
            if not st:#if stack id empty ->push
                st.append(i)
            else:
                if i==st[-1]:#found a duplicate adjacent
                    st.pop()
                else:
                    st.append(i)
        return "".join(st)
