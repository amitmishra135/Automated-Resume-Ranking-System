import subprocess
import os

def run_tests():
    # Run your unit tests here
    result = subprocess.run(['python', '-m', 'unittest', 'discover', 'tests'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Tests failed. Aborting deployment.")
        print(result.stdout)
        return False
    return True

def train_model():
    # Train the model
    subprocess.run(['python', 'model_training.py'])

def deploy():
    # In a real-world scenario, this might involve pushing to a production server
    print("Deploying the application...")
    # Example: subprocess.run(['ssh', 'user@server', 'cd /path/to/app && git pull && sudo systemctl restart app'])

def main():
    if run_tests():
        train_model()
        deploy()
        print("Deployment completed successfully.")

if __name__ == "__main__":
    main()