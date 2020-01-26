class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a=[]
        b=[]
        c=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        def s(i):
            if(i==len(digits)):
                d="".join(k for k in a)
                if(d!=''):
                    b.append(d)
            elif(digits[i]==1):
                s(i+1)
            else:
                for j in range(len(c[int(digits[i])-2])):
                    a.append(c[int(digits[i])-2][j])
                    s(i+1)
                    del a[-1]
        s(0)
        return b
