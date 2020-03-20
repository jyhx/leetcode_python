#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for mid in range(len(s)):
            # 以s[mid]为中心的回文字符串s[i:j]
            i = mid - len(ret) // 2
            j = mid + len(ret) // 2 + 1
            while i >= 0 and j <= len(s):
                if s[i:j] != s[i:j][::-1]:
                    break
                ret = s[i:j]
                i -= 1
                j += 1
            # 以s[mid,mid+1]为中心的回文字符串s[i:j]
            i = mid - len(ret) // 2
            j = mid + len(ret) // 2 + 2
            while i >= 0 and j <= len(s):
                if s[i:j] != s[i:j][::-1]:
                    break
                ret = s[i:j]
                i -= 1
                j += 1
        return ret
# @lc code=end
