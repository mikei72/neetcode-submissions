class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlNum(c):
            if ord('a') <= ord(c) <= ord('z') or \
               ord('A') <= ord(c) <= ord('Z') or \
               ord('0') <= ord(c) <= ord('9'):
                return True
            else:
                return False

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not isAlNum(s[left]):
                left += 1
            while left < right and not isAlNum(s[right]):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True