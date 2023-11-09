import subprocess

def install_dependencies():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install dependencies. {e}")

install_dependencies()