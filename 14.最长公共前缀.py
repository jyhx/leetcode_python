#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            ret = ''
            for i in range(len(strs[0])):
                char = strs[0][i]
                for j in range(1, len(strs)):
                    if len(strs[j]) <= i or strs[j][i] != char:
                        return ret
                ret += char
            return ret
        except:
            return ''
# @lc code=end
