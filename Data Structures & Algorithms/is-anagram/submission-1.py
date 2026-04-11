class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create a hashmap to count occurance of char in s
        # then check from t
        # time complexity: O(n)

        hashmap = dict() 
        for char in s: # O(n)
            if char not in hashmap: # O(1)
                hashmap[char] = 1
            else:
                hashmap[char] += 1 # O(1)
        # then we have a hashmap where key = char, value = # of occurance

        for char in t: # O(n)
            # if the char is not part of s, then not anagram
            if char not in hashmap: # O(1)
                return False

            # if the char is part of s, then minus 1 from occurance in s    
            else:
                hashmap[char] -= 1 # O(1)

        for char in hashmap: # O(n)
            if hashmap[char] != 0: # O(1)
                return False
        return True

        # # interesting solution, sort them and just check ==
        # # time complexity: O(nlogn) for sorting
        # return (sorted(s) == sorted(t))


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