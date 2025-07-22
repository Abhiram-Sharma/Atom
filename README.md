# Git Automate

This project contains a Python script that automates GitHub commits to a repository. It is designed to run continuously and make 5 commits with meaningful messages twice a day.

## Features

- Automates Git commits.
- Runs twice a day.
- Generates 5 commits in each run.
- Runs continuously.
- Can be deployed for free on services like GitHub Actions.

## How it works

The `main.py` script uses the `schedule` library to run a job twice a day. Each job consists of making 5 commits to the repository. The script modifies a file called `dummy_file.txt` in each commit.

## Usage

1.  Clone the repository.
2.  Install the required dependencies: `pip install schedule`
3.  Run the script: `python main.py`
