class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='[' or s[i]=='(':
                a.append(s[i])
            else:
                if len(a)==0:
                    return bool(0)
                elif s[i]==']' and a[-1]=='[':
                    del a[-1]
                elif s[i]=='}' and a[-1]=='{':
                    del a[-1]
                elif s[i]==')' and a[-1]=='(':
                    del a[-1]
                else:
                    return bool(0)
        if a==[]:
            return bool(1)
