import os
import subprocess
import sys

# Function to create a virtual environment
def create_virtualenv(venv_name):
    try:
        subprocess.run(["python", "-m", "venv", venv_name], check=True)
        print(f"Virtual environment '{venv_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment '{venv_name}': {e}")
        sys.exit(1)

# Function to activate a virtual environment
def activate_virtualenv(venv_name):
    try:
        activate_script = os.path.join(venv_name, "Scripts" if sys.platform == "win32" else "bin", "activate")
        subprocess.run([activate_script], shell=True, check=True)
        print(f"Virtual environment '{venv_name}' activated.")
    except subprocess.CalledProcessError as e:
        print(f"Error activating virtual environment '{venv_name}': {e}")
        sys.exit(1)

# Function to deactivate the current virtual environment
def deactivate_virtualenv():
    try:
        subprocess.run(["deactivate"], shell=True, check=True)
        print("Virtual environment deactivated.")
    except subprocess.CalledProcessError as e:
        print("Error deactivating virtual environment: {e}")
        sys.exit(1)

# Function to install a package in the current virtual environment
def install_package(package_name):
    try:
        subprocess.run(["pip", "install", package_name], check=True)
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package '{package_name}': {e}")
        sys.exit(1)

# Function to list installed packages in the current virtual environment
def list_installed_packages():
    try:
        result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, text=True, check=True)
        print("Installed packages in the current virtual environment:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error listing installed packages: {e}")
        sys.exit(1)

# Function to uninstall a package from the current virtual environment
def uninstall_package(package_name):
    try:
        subprocess.run(["pip", "uninstall", package_name, "-y"], check=True)
        print(f"Package '{package_name}' uninstalled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling package '{package_name}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Define the name of the virtual environment and package to install
    venv_name = "env"
    package_to_install = "requests"

    # Create and activate the virtual environment
    create_virtualenv(venv_name)
    activate_virtualenv(venv_name)

    # Install a package in the virtual environment
    install_package(package_to_install)

    # List installed packages in the virtual environment
    list_installed_packages()

    # Uninstall the package from the virtual environment
    uninstall_package(package_to_install)

    # Deactivate the virtual environment
    deactivate_virtualenv()