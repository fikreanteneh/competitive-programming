/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    
    function isPalindrome(s){
        for (let i = 0; i < s.length/2; i++){
            if (s[i] != s[s.length - i  - 1]) return false
        }
        
        return true
    }
    
    function dp(index){
        if (index == -1) return [[]]
        const possible = []
        for (let i = index; i >= 0; i--){
            const substring = s.substring(i, index + 1)
            if (!isPalindrome(substring)) continue
            dp(i - 1).forEach(element => {
                const newElement = [...element, substring]
                possible.push(newElement)
            })
        }
        return possible
    }
    return dp(s.length - 1)
};