var TimeLimitedCache = function() {
    this.dict = new Map()
    
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const found = this.dict.has(key)
    if (found){
        const timer = this.dict.get(key)[1]
        clearTimeout(timer)
    }
    this.dict.set(key, [
        value,
        setTimeout(() => {this.dict.delete(key)}, duration)
    ])
    return found
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.dict.has(key) ? this.dict.get(key)[0] : -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.dict.size
    
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */