class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1.replace(str2, "", 1)


str1 = "ABABAB"
str2 = "ABAB"


s = Solution()
print(s.gcdOfStrings(str1, str2))
