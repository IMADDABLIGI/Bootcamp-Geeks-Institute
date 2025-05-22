document.getElementById('libform').addEventListener('submit', function(event) {
    event.preventDefault();

    const noun = document.getElementById('noun').value;
    const adjective = document.getElementById('adjective').value;
    const person = document.getElementById('person').value;
    const verb = document.getElementById('verb').value;
    const place = document.getElementById('place').value;

    console.log(noun, adjective, person, verb, place);
    if (!noun || !adjective || !person || !verb || !place) {
        console.error('All fields must be filled out!');
        alert('Please fill out all the fields.');
        return;
    }

    const story = `Once upon a time in ${place}, there was a ${adjective} ${noun} named ${person} who loved to ${verb} all day long.`;
    document.getElementById('story').textContent = story;
});