// script.js

// Function to play sound by key
function playSound(key) {
  const audio = document.getElementById(key.toUpperCase());
  const button = document.querySelector(`button[data-key="${key.toUpperCase()}"]`);
  if (audio) {
    audio.currentTime = 0; // rewind to start
    audio.play();
    button.classList.add("playing");
    setTimeout(() => button.classList.remove("playing"), 100);
  }
}

// Keyboard press
document.addEventListener("keydown", (event) => {
  playSound(event.key);
});

// Mouse click
const buttons = document.querySelectorAll(".drum");
buttons.forEach(button => {
  button.addEventListener("click", function () {
    const key = this.getAttribute("data-key");
    playSound(key);
  });
});
