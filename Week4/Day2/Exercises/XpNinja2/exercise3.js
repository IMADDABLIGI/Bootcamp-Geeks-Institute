function findWordInString(str, word) {
  if (str.includes(word)) {
    return `The word "${word}" was found in the string.`;
  } else {
    return `The word "${word}" was not found in the string.`;
  }
}

const exampleString = "The quick brown fox jumps over the lazy dog.";

console.log(findWordInString(exampleString, "fox"));