/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const new_array = []
    n = arr.length
    for (let i = 0; i < n; i++){
        new_array.push(fn(arr[i], i))
    }
    return new_array
};