[[0, 1], [2, 3]].reduce(
  (acc, cur) => {
    return acc.concat(cur);
  },
  [1, 2],
);

// output will be [1, 2, 0, 1, 2, 3]
// Explanation:
// The reduce function starts with the initial value [1, 2].
// It then iterates over each sub-array in the input array [[0, 1], [2, 3]].