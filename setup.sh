#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "Starting setup..."

# Create directories
echo "Creating directories..."
mkdir -p assets/images
mkdir -p assets/css
mkdir -p assets/js

# Copy images
echo "Copying images..."
if cp static/images/* assets/images/; then
    echo -e "${GREEN}Images copied successfully${NC}"
else
    echo -e "${RED}Error copying images${NC}"
    exit 1
fi

# Create .nojekyll for GitHub Pages
touch .nojekyll

# Verify structure
echo "Verifying file structure..."
echo "assets/images contents:"
ls -la assets/images/

echo -e "${GREEN}Setup complete!${NC}" 