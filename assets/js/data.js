// Helper function to get correct image path
function getImagePath(imageName) {
    // Check if we're on GitHub Pages
    const isGitHubPages = window.location.hostname.includes('github.io');
    const basePath = isGitHubPages ? '/PythonGame' : '';
    return `${basePath}/assets/images/${imageName}`;
}

const gameData = {
    'easy': [
        {"image": getImagePath("python_logo.jpg"), "word": "PYTHON"},
        {"image": getImagePath("html_logo.png"), "word": "HTML"},
        {"image": getImagePath("css_code_snippet.jpg"), "word": "CSS"},
        {"image": getImagePath("binary_code.jpg"), "word": "BINARY"},
        {"image": getImagePath("function_diagram.jpg"), "word": "FUNCTION"},
    ],
    'average': [
        {"image": getImagePath("javascript_logo.jpg"), "word": "JAVASCRIPT"},
        {"image": getImagePath("database_diagram.jpg"), "word": "DATABASE"},
        {"image": getImagePath("algorithm_flow.jpg"), "word": "ALGORITHM"},
        {"image": getImagePath("react_logo.jpg"), "word": "REACT"},
        {"image": getImagePath("docker_logo.jpg"), "word": "DOCKER"},
    ],
    'hard': [
        {"image": getImagePath("kubernetes_arch.jpg"), "word": "KUBERNETES"},
        {"image": getImagePath("microservices.jpg"), "word": "MICROSERVICES"},
        {"image": getImagePath("blockchain.jpg"), "word": "BLOCKCHAIN"},
        {"image": getImagePath("machine_learning.jpg"), "word": "MACHINELEARNING"},
        {"image": getImagePath("cryptography.jpg"), "word": "CRYPTOGRAPHY"},
    ]
}; 