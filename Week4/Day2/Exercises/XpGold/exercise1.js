[1, 2, 3].map(num => {
  if (typeof num === 'number') return num * 2;
  return ;
});

// expected behavior is the double of each number in the array