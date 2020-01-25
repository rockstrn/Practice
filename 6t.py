class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a=[]
        j=0
        j1=numRows-1
        if(len(s)<=numRows or numRows==1):
            return s
        k=len(s)//(2*numRows-2)
        for i in range((len(s)+2*numRows-3)//(2*numRows-2)):
            a.append(s[j])
            j=j+2*numRows-2
        for r in range(1,numRows-1):
            for i in range(k+1):
                p=r+(2*numRows-2)*i
                if p<len(s):
                    a.append(s[p])
                p=p+2*numRows-2*r-2
                if p<len(s):
                    a.append(s[p])
        for i in range((len(s)+numRows-2)//(2*numRows-2)):
            a.append(s[j1])
            j1=j1+2*numRows-2  
        b=''.join(a)
        return b
