class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) {
            return false
        }
        let map = new Map()
        for (let i = 0; i < s.length; i++) {
            if (!map.has(s[i])) {
                map.set(s[i], 0)
            }
            map.set(s[i], map.get(s[i]) + 1)
            if (!map.has(t[i])) {
                map.set(t[i], 0)
            }
            map.set(t[i], map.get(t[i]) - 1)
        }
        // for (const [key,val] of map) {
        //     if (val != 0) {
        //         return false
        //     }
        // for (const key of map.keys()) {
        //     if (map.get(key) != 0) {
        //         return false
        //     }
        // }
        for (const val of map.values()) {
            if (val != 0) {
                return false
            }
        }
        return true
    }
        

}
