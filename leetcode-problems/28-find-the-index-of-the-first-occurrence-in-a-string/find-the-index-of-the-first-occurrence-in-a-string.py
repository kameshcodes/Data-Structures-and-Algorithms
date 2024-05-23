class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        while idx <= len(haystack)-len(needle):
            if haystack[idx]==needle[0] and haystack[idx:idx+len(needle)]==needle:
                return idx
            else:
                idx = idx + 1
        return -1










