const promise1 = Promise.resolve(3);
const promise2 = 42; // not a Promise, but gets wrapped by Promise.all
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo');
});

// Use Promise.all to wait for all the promises
Promise.all([promise1, promise2, promise3])
  .then((values) => {
    console.log("All Promises Resolved:", values);
    // Expected output: [3, 42, "foo"]
  })
  .catch((error) => {
    console.log("One of the promises failed:", error);
  });

/*
EXPLANATION:

Promise.all() takes an array of values (promises or non-promises).
- It returns a new Promise.
- It waits for **all** of them to be resolved.
- If all are successful → it gives an array of resolved values (in the same order).
- If **any** promise is rejected → the whole Promise.all() fails and jumps to `.catch()`.

In this case:
- promise1 resolves immediately to 3.
- promise2 is just a number (not a promise), so it is treated as Promise.resolve(42).
- promise3 resolves after 3 seconds to "foo".

Since none of them reject, you get:
[3, 42, "foo"]
*/
