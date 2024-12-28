/**
 * @param {Function} fn
 * @return {Function}
 */

function memoize(fn) {
    const memory = {}; // Local cache for each memoized function
    
    return function(...args) {
        const argKey = JSON.stringify(args); // Use JSON.stringify to generate a unique key
        
        if (argKey in memory) {
            return memory[argKey];
        } else {
            const result = fn(...args);
            memory[argKey] = result;
            return result;
        }
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