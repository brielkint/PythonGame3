class Game {
    constructor(difficulty) {
        this.difficulty = difficulty;
        this.questions = this.shuffleQuestions(gameData[difficulty]);
        this.currentIndex = 0;
        this.score = 0;
        this.timer = null;
        this.seconds = 0;
    }

    shuffleQuestions(questions) {
        return [...questions].sort(() => Math.random() - 0.5);
    }

    shuffleWord(word) {
        let letters = word.split('');
        let shuffled;
        do {
            shuffled = [...letters].sort(() => Math.random() - 0.5).join('');
        } while (shuffled === word);
        return shuffled;
    }

    getCurrentQuestion() {
        return this.questions[this.currentIndex];
    }

    checkAnswer(guess) {
        const correct = guess.toUpperCase() === this.getCurrentQuestion().word;
        if (correct) {
            const points = this.calculatePoints();
            this.score += points;
        }
        return {
            correct,
            points: correct ? this.calculatePoints() : 0,
            message: correct ? "Correct!" : "Try Again!"
        };
    }

    calculatePoints() {
        const timeBonus = Math.max(100 - this.seconds, 0);
        const difficultyMultiplier = {
            'easy': 1,
            'average': 1.5,
            'hard': 2
        }[this.difficulty];
        return Math.floor(timeBonus * difficultyMultiplier);
    }

    isGameOver() {
        return this.currentIndex >= this.questions.length - 1;
    }

    nextQuestion() {
        if (!this.isGameOver()) {
            this.currentIndex++;
            this.seconds = 0;
            return true;
        }
        return false;
    }

    startTimer(callback) {
        this.seconds = 0;
        this.timer = setInterval(() => {
            this.seconds++;
            callback(this.seconds);
        }, 1000);
    }

    stopTimer() {
        if (this.timer) {
            clearInterval(this.timer);
            this.timer = null;
        }
    }
}

// Game UI Controller
class GameUI {
    constructor() {
        this.game = null;
        this.setupEventListeners();
    }

    setupEventListeners() {
        document.getElementById('guess').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.checkAnswer();
            }
        });
    }

    init() {
        const difficulty = localStorage.getItem('selectedDifficulty') || 'easy';
        this.game = new Game(difficulty);
        this.updateUI();
        this.startTimer();
    }

    updateUI() {
        const question = this.game.getCurrentQuestion();
        document.getElementById('image').src = question.image;
        document.getElementById('scrambled').textContent = this.game.shuffleWord(question.word);
        document.getElementById('current-question').textContent = this.game.currentIndex + 1;
        document.getElementById('total-questions').textContent = this.game.questions.length;
        document.getElementById('score').textContent = this.game.score;
    }

    checkAnswer() {
        const guess = document.getElementById('guess').value.trim();
        if (!guess) return;

        const result = this.game.checkAnswer(guess);
        this.showResult(result.message, result.correct);

        if (result.correct) {
            document.getElementById('guess').disabled = true;
            this.game.stopTimer();
            setTimeout(() => {
                if (this.game.isGameOver()) {
                    this.endGame();
                } else {
                    this.game.nextQuestion();
                    this.updateUI();
                    document.getElementById('guess').value = '';
                    document.getElementById('guess').disabled = false;
                    document.getElementById('guess').focus();
                    this.startTimer();
                }
            }, 1500);
        }
    }

    showResult(message, isCorrect) {
        const result = document.getElementById('result');
        result.textContent = message;
        result.style.color = isCorrect ? "#28a745" : "#dc3545";
    }

    startTimer() {
        this.game.startTimer((seconds) => {
            const minutes = Math.floor(seconds / 60);
            const remainingSeconds = seconds % 60;
            document.getElementById('time').textContent = 
                `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
        });
    }

    endGame() {
        const gamesPlayed = parseInt(localStorage.getItem('gamesPlayed') || 0) + 1;
        const bestScore = Math.max(parseInt(localStorage.getItem('bestScore') || 0), this.game.score);
        
        localStorage.setItem('gamesPlayed', gamesPlayed);
        localStorage.setItem('bestScore', bestScore);
        
        alert(`Game Complete!\nFinal Score: ${this.game.score}`);
        window.location.href = 'index.html';
    }
}

// Initialize game when page loads
document.addEventListener('DOMContentLoaded', () => {
    const gameUI = new GameUI();
    gameUI.init();
}); 