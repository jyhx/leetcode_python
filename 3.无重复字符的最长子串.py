#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        i, ret = 0, 0
        # 最长子串为str[i:j+1]
        for j in range(len(s)):
            if s[j] in char_to_index:
                i = max(char_to_index[s[j]] + 1, i)
            char_to_index[s[j]] = j
            ret = max(ret, j - i + 1)
        return ret
# @lc code=end
