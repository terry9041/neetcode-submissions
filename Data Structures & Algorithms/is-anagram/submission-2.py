class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # time complexity: O(n)
        # memory complexity: O(n)

        # if they are of dif length,not anagram alrdy
        # O(1) to get array length
        if (len(s) != len(t)):
            return False

        # create a hashmap 
        # key: char, value: no of occurances
        # max size: n*2 -> O(n) if all char in s,t are distinct
        hashmap = dict()

        # O(n), n times for all O(1) operations
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]] -= 1
        
        # O(n), n times for all O(1) operations
        for char in hashmap:
            if hashmap[char] != 0:
                return False
        return True

        # # hashmap solution v2
        # # create a hashmap 
        # # key: char, value: no of occurances
        # # max size: n -> O(n) if all char in s distinct

        # if (len(s) != len(t)):
        #     return False

        # hashmap = dict()

        # # O(n), n times for all O(1) operations
        # for i in range(len(s)):
        #     if s[i] not in hashmap:
        #         hashmap[s[i]] = 1
        #     else:
        #         hashmap[s[i]] += 1
        
        # for i in range(len(s)):
        #     if t[i] not in hashmap:
        #         return False
        #     else:
        #         hashmap[t[i]] -= 1
        
        # # O(n), n times for all O(1) operations
        # for char in hashmap:
        #     if hashmap[char] != 0:
        #         return False
        # return True

        # # time complexity: O(nlogn)
        # # memory complexity: O(1)

        # if len(s) != len(t):
        #     return False
        # return sorted(s)==sorted(t)



        # naive solution, look at each elem of s1 and loop s2 to see if it's in s2
        # O(n*m)

        # necessity for anagram: same length
        # time complexity for getting array length: O(1)
        # if len(s) != len(t):
        #     return False

        # t = list(t)

        # for c1 in s: # O(n)
        #     isContain = False
        #     for ind in range(len(t)): # O(m)
        #         c2 = t[ind]
        #         if (c1==c2):
        #             isContain = True
        #             t[ind] = None
        #             break
        #     if not isContain:
        #         return False
        # return True