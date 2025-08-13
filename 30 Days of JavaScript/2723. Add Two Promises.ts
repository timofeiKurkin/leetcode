type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    return Promise.all([promise1, promise2]).then((nums) => nums[0] + nums[1])
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */