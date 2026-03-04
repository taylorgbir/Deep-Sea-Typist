<!DOCTYPE html>
<html>
<head>
<title>🌊 Ocean Rush Typing</title>
<style>
body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
    color: white;
    background: linear-gradient(to bottom, #001f3f, #003f5c, #2c7da0);
}

h1 {
    text-align: center;
    margin-top: 15px;
}

#controls, #stats {
    text-align: center;
    margin: 10px;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 8px;
    border: none;
    margin: 5px;
    cursor: pointer;
}

#input {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    padding: 12px;
    font-size: 18px;
    border-radius: 10px;
    border: none;
    width: 300px;
    text-align: center;
}

.word {
    position: absolute;
    font-size: 22px;
    white-space: nowrap;
    animation: swim linear forwards;
}

@keyframes swim {
    from { transform: translateX(-200px); }
    to { transform: translateX(120vw); }
}
</style>
</head>
<body>

<h1>🌊 Ocean Rush Typing</h1>

<div id="controls">
    <button id="startBtn">Start</button>
    <button id="stopBtn">Stop</button>
</div>

<div id="stats"></div>
<input id="input" placeholder="Type to catch..." disabled />

<script>
const words = [
    "coral","anchor","harbor","wave","tide","shell",
    "ocean","current","seabed","submarine","kelp",
    "dolphin","whirlpool","reef","compass","voyage",
    "storm","lighthouse","mariner","horizon",
    "treasure","pirate","shipwreck","captain"
];

let score, totalChars, correctChars, lives, timeLeft;
let highScore = localStorage.getItem("oceanHighScore") || 0;
let gameActive = false;
let spawnInterval, timerInterval, startTime;

const input = document.getElementById("input");
const stats = document.getElementById("stats");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

function updateStats() {
    let minutes = (Date.now() - startTime) / 60000;
    let wpm = minutes > 0 ? Math.round((correctChars/5)/minutes) : 0;
    let accuracy = totalChars > 0 ? Math.round((correctChars/totalChars)*100) : 100;

    stats.innerHTML =
        `Score: ${score} | Lives: ${lives} | Time: ${timeLeft}s | WPM: ${wpm} | Accuracy: ${accuracy}% | High Score: ${highScore}`;
}

function createWord() {
    if(!gameActive) return;

    const wordDiv = document.createElement("div");
    wordDiv.className = "word";

    const word = words[Math.floor(Math.random()*words.length)];
    wordDiv.textContent = "🐠 " + word;
    wordDiv.dataset.word = word;

    wordDiv.style.top = Math.random() * (window.innerHeight - 150) + "px";
    wordDiv.style.animationDuration = (6 + Math.random()*3) + "s";

    document.body.appendChild(wordDiv);

    wordDiv.addEventListener("animationend", () => {
        if(gameActive) {
            lives--;
            if(lives <= 0) stopGame();
            updateStats();
        }
        wordDiv.remove();
    });
}

function startGame() {
    if(gameActive) return;

    score = 0;
    totalChars = 0;
    correctChars = 0;
    lives = 5;
    timeLeft = 60;
    startTime = Date.now();
    gameActive = true;

    input.disabled = false;
    input.value = "";
    input.focus();

    spawnInterval = setInterval(createWord, 2000);

    timerInterval = setInterval(() => {
        timeLeft--;
        if(timeLeft <= 0) stopGame();
        updateStats();
    }, 1000);

    updateStats();
}

function stopGame() {
    gameActive = false;
    clearInterval(spawnInterval);
    clearInterval(timerInterval);
    input.disabled = true;

    document.querySelectorAll(".word").forEach(w => w.remove());

    if(score > highScore) {
        highScore = score;
        localStorage.setItem("oceanHighScore", highScore);
    }

    updateStats();
}

input.addEventListener("input", function() {
    if(!gameActive) return;

    const value = input.value.trim().toLowerCase();
    totalChars++;

    document.querySelectorAll(".word").forEach(wordDiv => {
        if(value === wordDiv.dataset.word) {
            score++;
            correctChars += wordDiv.dataset.word.length;
            wordDiv.remove();
            input.value = "";
        }
    });

    updateStats();
});

startBtn.addEventListener("click", startGame);
stopBtn.addEventListener("click", stopGame);

updateStats();
</script>

</body>
</html>
