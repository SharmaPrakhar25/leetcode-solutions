/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let numStr = x.toString();
    let result = numStr.split('').reverse().join('');
    return numStr === result;
};