// public/script.js

let currentCorrect = '';
let score = 0;

function fetchQuestion() {
  fetch('/api/question')
    .then(res => res.json())
    .then(data => {
      currentCorrect = data.correct;
      document.getElementById('emoji').textContent = data.emoji;
      const optionsDiv = document.getElementById('options');
      optionsDiv.innerHTML = '';
      data.options.sort(() => Math.random() - 0.5).forEach(option => {
        const btn = document.createElement('button');
        btn.textContent = option;
        btn.onclick = () => submitGuess(option);
        optionsDiv.appendChild(btn);
      });
    });
}

function submitGuess(guess) {
  fetch('/api/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ guess, correct: currentCorrect })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById('feedback').textContent = data.correct
        ? '✅ Correct!'
        : '❌ Wrong!';
      document.getElementById('score').textContent = data.score;
      setTimeout(fetchQuestion, 1000);
    });
}

document.getElementById('leaderboard-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  fetch('/api/submit-score', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
  }).then(() => {
    document.getElementById('leaderboard-form').style.display = 'none';
    fetchLeaderboard();
  });
});

function fetchLeaderboard() {
  fetch('/api/leaderboard')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById('leaderboard');
      list.innerHTML = '';
      data.leaderboard.forEach(entry => {
        const li = document.createElement('li');
        li.textContent = `${entry.name}: ${entry.score}`;
        list.appendChild(li);
      });
    });
}

fetchQuestion();
fetchLeaderboard();
