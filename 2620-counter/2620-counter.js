/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let x = n
    let c = 0
    
    return function() {
        if (c==0){
            c+=1
            return x
        }
        x+=1
        return x;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */