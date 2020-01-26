class Solution:
    def romanToInt(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            if s[i]=='M':
                a=a+1000
            if s[i]=='D':
                a=a+500
            if s[i]=='C':
                if i<len(s)-1 and (s[i+1]=='D' or s[i+1]=='M'):
                    a=a-100
                else:
                    a=a+100
            if s[i]=='L':
                a=a+50
            if s[i]=='X' :
                if i<len(s)-1 and (s[i+1]=='L' or s[i+1]=='C'):
                    a=a-10
                else:
                    a=a+10
            if(s[i]=='V'):
                a=a+5
            if(s[i]=='I'):
                if i<len(s)-1 and (s[i+1]=='V' or s[i+1]=='X'):
                    a=a-1
                else:
                    a=a+1
        return a
