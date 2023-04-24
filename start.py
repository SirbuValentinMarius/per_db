import subprocess  # Import the subprocess module


# Generează fișierul requirements.txt
with open("requirements.txt", "w") as f:
    subprocess.run(["python", "-m", "pip", "freeze"], stdout=f)

# Instalează modulele enumerate în fișierul requirements.txt
subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])

# Șterge fișierul requirements.txt
subprocess.run(["rm", "requirements.txt"])



subprocess.Popen(["python", "per_db.py"], creationflags=subprocess.CREATE_NO_WINDOW)