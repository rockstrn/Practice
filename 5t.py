class Solution:
    def longestPalindrome(self, s: str) -> str:
        def j(i):
            p=1
            a=min(i,len(s)-i-1)
            for k in range(1,a+1):
                if s[i-k]!=s[i+k]:
                    b=k-1
                    p=0
                    break
            if p:
                b=a
            return 2*b+1
        def ou(i):
            if s[i]!=s[i+1]:
                return 1
            else:
                a=min(i,len(s)-i-2)
                b=0
                p=1
                for k in range(1,a+1):
                    if s[i-k]!=s[i+1+k]:
                        b=k-1
                        p=0
                        break
                if p:
                    b=a
                return 2*b+2
        h,t=1,0
        for i in range(len(s)-1):
            a=max(ou(i),j(i))
            if a>h:
                h=a
                t=i
        if h%2==0:
            return s[t-(h//2)+1:t+(h//2)+1]
        if h%2==1:
            return s[t-(h//2):t+(h//2)+1]
