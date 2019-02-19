# Code for Conversational AI session 

# Installation 

*Tested on Python 3.6*

- Clone/download this repository 
`git clone https://github.com/nlp-stuff/conversational-ai-code.git`

- Install required package/libraries
`pip install requirements.txt`

# Usage

Each directory contains code for specific session, navigate to readme file of respective directory



# Usage Azure Notebook (NLP directory)

- Open **terminal** in Jupyter Notebook

- Navigate to nlp folder
`cd library/nlp`

- Pull latest code:
```bash
git reset --hard HEAD
git pull origin master
```

- Install required dependencies 
`pip3 install -r requirements.txt --user`

- Install nltk packages, type following in terminal
`python3 nltk_download.py`

- Execute chatbot script
`python3 chatbot.py`