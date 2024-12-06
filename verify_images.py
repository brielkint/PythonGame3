import os

def verify_images():
    image_dir = os.path.join('static', 'images')
    required_images = [
        'python_logo.jpg',
        'html_logo.png',
        'css_code_snippet.jpg',
        'binary_code.jpg',
        'function_diagram.jpg',
        'javascript_logo.jpg',
        'database_diagram.jpg',
        'algorithm_flow.jpg',
        'react_logo.jpg',
        'docker_logo.jpg',
        'kubernetes_arch.jpg',
        'microservices.jpg',
        'blockchain.jpg',
        'machine_learning.jpg',
        'cryptography.jpg'
    ]

    # Check if directory exists
    if not os.path.exists(image_dir):
        print(f"Error: Directory {image_dir} does not exist!")
        return False

    # Check each required image
    missing_images = []
    for image in required_images:
        image_path = os.path.join(image_dir, image)
        if not os.path.exists(image_path):
            missing_images.append(image)

    if missing_images:
        print("Missing images:")
        for image in missing_images:
            print(f"- {image}")
        return False

    print("All images verified successfully!")
    return True

if __name__ == "__main__":
    verify_images() 