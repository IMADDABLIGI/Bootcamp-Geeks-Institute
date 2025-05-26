(function (children, partnerName, location, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${children} kids.`;
    
    const resultElement = document.getElementById('result');
    resultElement.textContent = sentence;
}
)(8, 'Saadiya', 'Had Soualem', 'Software Engineer');