#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        flag = bool(s) and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (flag and self.isMatch(s[1:], p))
        else:
            return flag and self.isMatch(s[1:], p[1:])


# @lc code=end
