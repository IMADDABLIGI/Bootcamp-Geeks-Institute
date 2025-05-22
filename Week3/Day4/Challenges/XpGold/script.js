const input = document.getElementById('lettersOnly');

input.addEventListener('input', function () {
    // Replace anything that's not a-z or A-Z with an empty string
    this.value = this.value.replace(/[^a-zA-Z]/g, '');
    console.log(this.value);
});


// console.log("value ->>" , input.value);