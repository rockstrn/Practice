class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=[]
        if(x<0):
            return bool(0)
        while(x!=0):
            a.append(x%10)
            x=x//10
        i=0
        j=len(a)-1
        while i < j:
            if a[i]!=a[j]:
                return bool(0)
            i=i+1
            j=j-1
        return bool(1)
