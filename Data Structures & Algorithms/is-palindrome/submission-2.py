class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
         # time complexity: O(n) due to full list scan and while loop
        # space complexity: O(n) due to new list
        s = [char.lower() for char in s if char.isalnum()]
        l,r = 0, len(s)-1
        while (l<=r):
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        return True

        # # time complexity: O(n)
        # # memory complexity: O(1)
        # # when checking condition in while loop
        # # 1. increment first? if you alrdy checked the char, then yes, else no
        # # 2. which elem to check for isalnum()? the current one
        # # 3. check if in range, need +- 1? no, rmb that its only for validating current index that we are gonna check char on 

        # l,r = 0, len(s)-1

        # while  l < len(s) and not s[l].isalnum():
        #     l += 1 

        # while  r >=0 and not s[r].isalnum():
        #     r -= 1

        # while(l<=r):

        #     if s[l].lower() != s[r].lower():
        #         return False

        #     l += 1
        #     while  l < len(s) and not s[l].isalnum():
        #         l += 1

        #     r -=1
        #     while  r >=0 and not s[r].isalnum():
        #         r -= 1

        # return True

        


