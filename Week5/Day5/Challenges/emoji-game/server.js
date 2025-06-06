import express from 'express';
import { emojis } from './emojis.js';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const PORT = 5000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

let leaderboard = [];
let playerScore = 0;

function getNewQuestion() {
  const correct = emojis[Math.floor(Math.random() * emojis.length)];
  const options = new Set([correct.name]);
  while (options.size < 4) {
    const random = emojis[Math.floor(Math.random() * emojis.length)].name;
    options.add(random);
  }
  return { emoji: correct.emoji, correct: correct.name, options: [...options] };
}

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});

app.get('/api/question', (req, res) => {
  const question = getNewQuestion();
  res.json(question);
});

app.post('/api/guess', (req, res) => {
  const { guess, correct } = req.body;
  const isCorrect = guess === correct;
  if (isCorrect) playerScore += 1;
  res.json({ correct: isCorrect, score: playerScore });
});

app.post('/api/submit-score', (req, res) => {
  const { name } = req.body;
  leaderboard.push({ name, score: playerScore });
  leaderboard.sort((a, b) => b.score - a.score);
  playerScore = 0;
  res.json({ leaderboard: leaderboard.slice(0, 5) });
});

app.get('/api/leaderboard', (req, res) => {
  res.json({ leaderboard: leaderboard.slice(0, 5) });
});

app.listen(PORT, () => {
  console.log(`🎮 Emoji Game Server running at http://localhost:${PORT}`);
});
