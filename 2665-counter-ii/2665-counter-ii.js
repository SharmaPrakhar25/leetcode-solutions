/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    curr = init
    return {
        increment: () => {
            this.curr += 1
            return this.curr
        },
        decrement: () => {
            this.curr -= 1
            return this.curr
        },
        reset: () => {
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