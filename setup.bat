@echo off
echo Starting setup...

:: Create directories
echo Creating directories...
if not exist "public\static\images" mkdir "public\static\images"

:: Copy images
echo Copying images...
xcopy /Y "static\images\*" "public\static\images\"

:: Create placeholder
echo Creating placeholder...
copy /Y "public\static\images\python_logo.jpg" "public\static\images\placeholder.jpg"

:: Verify images
echo Verifying images...
set REQUIRED_IMAGES=python_logo.jpg html_logo.png css_code_snippet.jpg binary_code.jpg function_diagram.jpg javascript_logo.jpg database_diagram.jpg algorithm_flow.jpg react_logo.jpg docker_logo.jpg kubernetes_arch.jpg microservices.jpg blockchain.jpg machine_learning.jpg cryptography.jpg

for %%i in (%REQUIRED_IMAGES%) do (
    if not exist "public\static\images\%%i" (
        echo Missing image: %%i
        exit /b 1
    )
)

:: Create .nojekyll
echo. > .nojekyll

:: List contents
echo Verifying file structure...
dir "public\static\images"

echo Setup complete!
pause 