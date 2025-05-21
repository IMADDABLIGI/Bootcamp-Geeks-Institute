const switchCase = (str) => {
    let swapped = '';

  for (let char of str) {
    if (char === char.toUpperCase()) {
      swapped += char.toLowerCase();
    } else {
      swapped += char.toUpperCase();
    }
  }

  return swapped;
}

console.log(switchCase("Hello World from ImAd"));