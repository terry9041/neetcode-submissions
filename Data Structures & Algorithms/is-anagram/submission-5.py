class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False # impossible anagram
        elif len(s1) == 0:
            return True
        hashmap = dict()
        for i in range(len(s1)):
            if s1[i] in hashmap:
                hashmap[s1[i]] += 1
            else:
                hashmap[s1[i]] = 1
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
            else:
                hashmap[s2[i]] = -1
        # if all value in pair is zero, the frequecies are all the same
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True

        # input: 2 strings
# output: 1 bool
# return true if anagram, false if not

# assumptions/clarify
# 1. can it be empty? yes
# 2. what is anagram? -> same word but with char rearranged
# 3. lowercase only

# examples
# Input: s = "racecar", t = "carrace"
# Output: true
# Input: s = "", t = ""
# Output: true
# Input: s = "raceca", t = "carrace"
# Output: false

# naive solution
# two hashmaps, for storing pair of char: freq in two strings sep
# two loops to fill in two hashmaps
# SC: O(2n) TC: O(2n) where N is max len of s1 s2

# sort the strings
# then compare
# SC: O(1) TC: O(nlogn)

# better: use char hashmap
# SC: O(n) TC: O(k) distinct chars

    

