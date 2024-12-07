#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "Starting setup..."

# Required images
REQUIRED_IMAGES=(
    "python_logo.jpg"
    "html_logo.png"
    "css_code_snippet.jpg"
    "binary_code.jpg"
    "function_diagram.jpg"
    "javascript_logo.jpg"
    "database_diagram.jpg"
    "algorithm_flow.jpg"
    "react_logo.jpg"
    "docker_logo.jpg"
    "kubernetes_arch.jpg"
    "microservices.jpg"
    "blockchain.jpg"
    "machine_learning.jpg"
    "cryptography.jpg"
)

# Create directories
echo "Creating directories..."
mkdir -p public/static/images

# Copy images
echo "Copying images..."
if cp static/images/* public/static/images/; then
    echo -e "${GREEN}Images copied successfully${NC}"
else
    echo -e "${RED}Error copying images${NC}"
    exit 1
fi

# Create placeholder
cp public/static/images/python_logo.jpg public/static/images/placeholder.jpg

# Verify images
echo "Verifying images..."
for img in "${REQUIRED_IMAGES[@]}"; do
    if [ ! -f "public/static/images/$img" ]; then
        echo -e "${RED}Missing image: $img${NC}"
        exit 1
    fi
done

echo -e "${GREEN}All images verified!${NC}"

# Create .nojekyll for GitHub Pages
touch .nojekyll

# Verify structure
echo "Verifying file structure..."
echo "public/static/images contents:"
ls -la public/static/images/

echo -e "${GREEN}Setup complete!${NC}" 