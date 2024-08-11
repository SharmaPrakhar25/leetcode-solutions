/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    const function_array = [...functions]
    const function_array_length = function_array.length
    return function(x) {
        let result = x;
        for(let i=function_array_length-1; i>=0; i--){
            result = function_array[i](result)
        }
        return result
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */