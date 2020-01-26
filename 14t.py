class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for j in strs:
                if len(j)-1<i or j[i]!=strs[0][i]:
                    return j[:i]
        return strs[0]
