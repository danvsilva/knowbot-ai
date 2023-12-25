# knowbot-ai
![](/images/knowbot-cli.png?raw=true "knowbot-cli")
---
Simple Q&A GPT bot for the command line.

## Installation
Clone the repository and install the dependencies with Poetry:

**Note:** This project requires Python 3.6 or higher and Poetry.

```bash
git clone https://github.com/danvsilva/knowbot-ai.git
cd knowbot-ai
poetry install
```

## Usage
There are a few ways we can execute the program. The first is to run the script directly using Poetry:
```bash
cd src
export OPENAI_API_KEY=<your key>
poetry run python knowbot_ai/main.py --question="What is the meaning of life?"
```

The second way is to create a shell script calling the Python script with Poetry:
```bash
#!/bin/zsh
poetry --project /path/to/repo run python3 /path/to/repo/knowbot_ai/main.py --question=$1
```

This quick script runs the Python script using Poetry, so there's no need to activate a virtual environment. Now we can run the script like so:
```bash
./knowbot.sh "What is the meaning of life?"
```

I personally like to add the script to my path so I can run it from anywhere:
```bash
export PATH=$PATH:<path to cloned repo>/knowbot_ai
alias knowbot="knowbot.sh"
knowbot "What is the meaning of life?"
```