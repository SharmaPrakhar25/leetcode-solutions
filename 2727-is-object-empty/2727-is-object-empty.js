/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if(Array.isArray(obj) && obj.length > 0){
        return false
    }else if (typeof obj === 'object' && Object.keys(obj).length > 0){
        return false
    }
    return true   
};