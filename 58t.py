class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(' ')
        if len(s)==0:
            return 0
        for i in range(1,len(s)+1):
            if(s[-i]==' '):
                break
        if s[-i]==' ':
            return i-1
        else:
            return i
