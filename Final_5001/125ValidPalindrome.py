'''
(Leetcode ​125) ​Valid Palindrome
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers i and j
        i = 0
        j = len(s) - 1
        # move the pointer until find two alphanumeric characters,
        # compare the value and return False if not equal
        # after comparision, move the pointer and begin another while loop
        # quit the while loop when i==j
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # if two values are not equal, return False and quit while loop
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        # i==j means going through all the characters and don't find
        # alphanumeric characters not equal, determins the string is palindrome.
        return True
