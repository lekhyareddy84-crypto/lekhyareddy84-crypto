class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while prefix and not word.startswith(prefix):
                prefix = prefix[:-1]
               
        return prefix
        