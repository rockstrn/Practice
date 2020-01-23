class Solution:
    def myAtoi(self, str: str) -> int:
        k,l=0,len(str)
        b=0
        a=['1','2','3','4','5','6','7','8','9','0']
        if(len(str)==0):
            return 0
        for i in range(len(str)):
            if(str[i]!=' '):
                k=i   
                break       
        for j in range(k+1,len(str)):
            if(str[j] not in a):
                l=j
                break
        if(str[k]=='+'):
            if(k+1>=len(str) or str[k+1] not in a):
                return 0
            else:
                f=1
                k=k+1
        elif(str[k]=='-'):
             if(k+1>=len(str) or str[k+1] not in a):
                return 0
             else:
                f=-1
                k=k+1
        elif (str[k] in a):
            f=1  
        else:
            return 0
        for i in range (k,l):
            if(f>0):
                if(b>2**31//10 or b==2**31//10 and int(str[i])>6):
                    return 2**31-1
            if(f<0):
                if(b>2**31//10 or b==2**31//10 and int(str[i])>7):
                    return -2**31
            b=b*10
            b=b+int(str[i])
        b=b*f
        return b
