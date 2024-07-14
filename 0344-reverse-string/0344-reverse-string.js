/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    s.reverse()
    return s
    
    for (let i = 0; i < s.length / 2; i++) {
        let [first, last] = [s[i], s[s.length - i - 1]];
        s[i] = last;
        s[s.length - i - 1] = first;
    }
    return s.join("");
};