class Solution:
    def peek_stack(self, stack):
        if stack:
            return stack[-1]
        else:
            return None

    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(0, len(s)):
            t = s[i]
            if t == ')':
                sb = []
                while len(st) > 0 and self.peek_stack(st) != '(':
                    sb.append(st.pop())
                st.pop()
                for j in range(0, len(sb)):
                    st.append(sb[j])
            else:
                st.append(t)
        res = ""
        while len(st) > 0:
            res += st.pop()
        return res[::-1]
