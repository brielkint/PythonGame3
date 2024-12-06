from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Game data organized by difficulty
game_data = {
    'easy': [
        {"image": "python_logo.jpg", "word": "PYTHON"},
        {"image": "html_logo.png", "word": "HTML"},
        {"image": "css_code_snippet.jpg", "word": "CSS"},
        {"image": "binary_code.jpg", "word": "BINARY"},
        {"image": "function_diagram.jpg", "word": "FUNCTION"},
    ],
    'average': [
        {"image": "javascript_logo.jpg", "word": "JAVASCRIPT"},
        {"image": "database_diagram.jpg", "word": "DATABASE"},
        {"image": "algorithm_flow.jpg", "word": "ALGORITHM"},
        {"image": "react_logo.jpg", "word": "REACT"},
        {"image": "docker_logo.jpg", "word": "DOCKER"},
    ],
    'hard': [
        {"image": "kubernetes_arch.jpg", "word": "KUBERNETES"},
        {"image": "microservices.jpg", "word": "MICROSERVICES"},
        {"image": "blockchain.jpg", "word": "BLOCKCHAIN"},
        {"image": "machine_learning.jpg", "word": "MACHINELEARNING"},
        {"image": "cryptography.jpg", "word": "CRYPTOGRAPHY"},
    ]
}

@app.route('/')
def homepage():
    """Homepage with difficulty selection."""
    return render_template('homepage.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    """Game logic: fetch and update the game state."""
    if request.method == 'POST':
        difficulty = request.json.get('difficulty', 'easy')
        questions = random.sample(game_data[difficulty], len(game_data[difficulty]))
        
        questions_data = []
        for question in questions:
            word_list = list(question['word'])
            random.shuffle(word_list)
            scrambled = ''.join(word_list)
            
            # Make sure scrambled word is different from original
            while scrambled == question['word']:
                random.shuffle(word_list)
                scrambled = ''.join(word_list)
                
            questions_data.append({
                "image": question["image"],
                "scrambled": scrambled,
                "correct_word": question['word']
            })
        
        return jsonify(questions_data)
    
    difficulty = request.args.get('difficulty', 'easy')
    return render_template('index.html', difficulty=difficulty)

@app.route('/check', methods=['POST'])
def check():
    """Check the player's answer."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"correct": False, "message": "No data received"}), 400

        user_guess = data.get('guess', '').strip()
        correct_word = data.get('correct_word', '').strip()

        if not user_guess or not correct_word:
            return jsonify({"correct": False, "message": "Input cannot be empty!"}), 400

        # Convert both to uppercase for comparison
        user_guess = user_guess.upper()
        correct_word = correct_word.upper()

        # Compare the answers
        if user_guess == correct_word:
            return jsonify({
                "correct": True,
                "message": "Correct!"
            })
        else:
            return jsonify({
                "correct": False,
                "message": "Try Again!"
            })

    except Exception as e:
        return jsonify({"correct": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)