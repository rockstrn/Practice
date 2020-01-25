class Solution:
    def reverse(self, x: int) -> int:
        a=[]
        b=0
        if(x<0):
            f=-1
        else:
            f=1
        x=x*f
        while((x+9)//10!=0):
            a.append(x%10)
            x=x//10
        for i in range(len(a)):
            if f<0:
                if(b>2**31//10 or (b==2**31 and a[i]>7)):
                    return 0
            else:
                if(b>2**31//10 or (b==2**31 and a[i]>6)):
                    return 0
            b=b*10
            b=b+a[i]
        b=b*f
        return b
