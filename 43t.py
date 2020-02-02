class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i1=len(num1)-1
        i=i1
        j1=len(num2)-1
        j=j1
        a=0
        while i>=0:
            j=j1
            while j>=0:
                a=a+int(num1[i])*int(num2[j])*10**(i1+j1-i-j)
                j=j-1
            i=i-1
        return str(a)
