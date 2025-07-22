import os
import schedule
import time
from datetime import datetime

REPO_PATH = r"E:\Temp Files\projects\gemini\GitAutomate"

def make_commit():
    try:
        os.chdir(REPO_PATH)
        with open("dummy_file.txt", "a") as f:
            f.write(f"Commit made at {datetime.now()}\n")
        os.system("git add .")
        os.system(f"git commit -m \"Automated commit at {datetime.now()}\"")
        os.system("git push")
        print(f"Commit made at {datetime.now()}")
    except Exception as e:
        print(f"Error making commit: {e}")

def job():
    for _ in range(5):
        make_commit()
        time.sleep(1) 

schedule.every().day.at("10:00").do(job)
schedule.every().day.at("22:00").do(job)

if __name__ == "__main__":
    print("Starting Git Automate script...")
    job() # Run once on startup
    while True:
        schedule.run_pending()
        time.sleep(1)
