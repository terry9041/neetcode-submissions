class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # this solutions reduce hassle in checking alnum but use more spaces
        # memory complexity: O(n)
        # time complexity: O(n)
        # rmb to increment and also it's len-1 for last elem
        l,r = 0, len(s)-1
        while (l<len(s) and (not (s[l].isalnum()))):
            l += 1
        while (r>=0 and (not (s[r].isalnum()))):
            r -= 1
        while (l <=r):
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            while (l<len(s) and (not (s[l].isalnum()))):
                l += 1
            r -=1
            while (r>=0 and (not (s[r].isalnum()))):
                r -= 1
        return True