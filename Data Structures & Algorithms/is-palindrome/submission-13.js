function isLetter(str) {
  return str.length === 1 && str.match(/[a-z0-9]/i);
}

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

    isPalindrome(s) {
        let l = 0
        let r = s.length-1
        while (l<r) {
            while ((l<r) && !isLetter(s[l])) {
                l ++
            }
            while ((l<r) && !isLetter(s[r])) {
                r --
            }
            if (s[l].toLowerCase() != s[r].toLowerCase()) {
                return false
            }
            l ++
            r --
        }
        return true
    }

    

}
