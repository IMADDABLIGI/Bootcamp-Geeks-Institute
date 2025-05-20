// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.


let sentence = "The bootcamp is not that bad, I like it";

let wordNot = sentence.indexOf("not")

// console.log(wordNot)

let wordBad = sentence.indexOf("bad")

if (wordBad > wordNot){
    result = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    // console.log(result)
}
else 
    result = sentence;

console.log(result);
