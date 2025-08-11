type Counter = {
    increment: () => number;
    decrement: () => number;
    reset: () => number;
};

function createCounter(init: number): Counter {
    let counter = init;
    return {
        increment: function () {
            return ++counter;
        },
        decrement: function () {
            return --counter;
        },
        reset: function () {
            counter = init;
            return counter;
        },
    };
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

export {}