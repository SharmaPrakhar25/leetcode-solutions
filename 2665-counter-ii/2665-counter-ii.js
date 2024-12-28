/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        curr: init,
        increment: function() {
            this.curr += 1
            return this.curr
        },
        decrement: function() {
            this.curr -= 1
            return this.curr
        },
        reset: function() {
            this.curr = init
            return this.curr
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */