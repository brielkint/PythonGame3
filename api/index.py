from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
import random
import os
from pathlib import Path

# Update template and static folders configuration
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public'))

app = Flask(__name__, 
    template_folder=template_dir,
    static_folder=static_dir,
    static_url_path='')

# Update game data with correct image paths
game_data = {
    'easy': [
        {"image": "/static/images/python_logo.jpg", "word": "PYTHON"},
        {"image": "/static/images/html_logo.png", "word": "HTML"},
        {"image": "/static/images/css_code_snippet.jpg", "word": "CSS"},
        {"image": "/static/images/binary_code.jpg", "word": "BINARY"},
        {"image": "/static/images/function_diagram.jpg", "word": "FUNCTION"},
    ],
    'average': [
        {"image": "/static/images/javascript_logo.jpg", "word": "JAVASCRIPT"},
        {"image": "/static/images/database_diagram.jpg", "word": "DATABASE"},
        {"image": "/static/images/algorithm_flow.jpg", "word": "ALGORITHM"},
        {"image": "/static/images/react_logo.jpg", "word": "REACT"},
        {"image": "/static/images/docker_logo.jpg", "word": "DOCKER"},
    ],
    'hard': [
        {"image": "/static/images/kubernetes_arch.jpg", "word": "KUBERNETES"},
        {"image": "/static/images/microservices.jpg", "word": "MICROSERVICES"},
        {"image": "/static/images/blockchain.jpg", "word": "BLOCKCHAIN"},
        {"image": "/static/images/machine_learning.jpg", "word": "MACHINELEARNING"},
        {"image": "/static/images/cryptography.jpg", "word": "CRYPTOGRAPHY"},
    ]
}

def verify_images():
    """Verify all images exist in static/images directory"""
    missing_images = []
    for difficulty in game_data:
        for item in game_data[difficulty]:
            image_path = os.path.join('static', 'images', item['image'].split('/')[-1])
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

# Add static file serving route
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_dir, filename)

@app.route('/debug-images')
def debug_images():
    """Debug endpoint to check image paths"""
    image_paths = []
    for difficulty in game_data:
        for item in game_data[difficulty]:
            full_path = os.path.join(static_dir, item['image'].lstrip('/'))
            exists = os.path.exists(full_path)
            image_paths.append({
                'path': item['image'],
                'full_path': full_path,
                'exists': exists
            })
    return jsonify(image_paths)

if __name__ == '__main__':
    app.run() 