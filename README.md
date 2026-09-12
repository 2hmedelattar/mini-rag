# Mini-RAG

This is a minimal implementation of the RAG model for question answering.

## Requirements 

- Python 3.11 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here]()
2) Create a new environment using the following command:
```bash 
$ conda create -n Mini-RAG-App python = 3.8
```
3) Activate the environment:
```bash 
$ conda activate Mini-RAG-App
```


### (Optional) Setup your command line for better readability
#### For Windows
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

#### For Mac
```bash
export PS1="%F{green}%n@%m:%~%f
$ "
```

## Installation 

### Install the required packages
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables 
```bash
$ cp .env.example .env
```

Setup your environment variables in the `.env` file . Like `OPENAI_API_KEY` value.
