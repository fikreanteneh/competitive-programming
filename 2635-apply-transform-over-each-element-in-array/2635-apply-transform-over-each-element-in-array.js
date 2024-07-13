/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    return arr.map((element, index) => fn(element, index))
    for (let i = 0; i < arr.length; i++){
        arr[i] = fn(arr[i], i)
    }
    return arr
};