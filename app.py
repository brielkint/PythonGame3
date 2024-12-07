from flask import Flask, render_template, request, jsonify, url_for
import random
import os

# Adjust the app configuration for static folder if needed
app = Flask(__name__, static_folder='public/static', static_url_path='/static')

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

def verify_images():
    """Verify all images exist in public/static/images directory"""
    missing_images = []
    for difficulty in game_data:
        for item in game_data[difficulty]:
            # Adjust path for public/static/images
            image_path = os.path.join('public', 'static', 'images', item['image'])
            if not os.path.exists(image_path):
                missing_images.append(item['image'])
    
    if missing_images:
        print("Warning: Missing images:", missing_images)

# Verify images on startup
verify_images()

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
        
        # Debug print
        print(f"Serving images for difficulty {difficulty}:")
        for q in questions:
            print(f"- {q['image']}")
        
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
