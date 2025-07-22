import os
from datetime import datetime
import time

REPO_PATH = os.getcwd()

def make_commit():
    try:
        os.chdir(REPO_PATH)
        with open("dummy_file.txt", "a") as f:
            f.write(f"Commit made at {datetime.now()}\n")
        os.system("git add .")
        os.system(f"git commit -m \"Automated commit at {datetime.now()}\"")
        print(f"Commit created at {datetime.now()}")
    except Exception as e:
        print(f"Error creating commit: {e}")

if __name__ == "__main__":
    for i in range(5):
        print(f"Running commit #{i+1}")
        make_commit()
        time.sleep(1)
    
    print("\nPushing to remote...")
    os.system("git push")
    print("Push successful.")