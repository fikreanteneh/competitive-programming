/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map()
    const result = Symbol()
    return (...params) => {
        let currentCache = cache;
        for(const param of params) {
            if (!currentCache.has(param)) {
                currentCache.set(param, new Map());
            }
            currentCache = currentCache.get(param);
        }

        if (currentCache.has(result)) return currentCache.get(result);
        currentCache.set(result, fn(...params));
        return currentCache.get(result);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */