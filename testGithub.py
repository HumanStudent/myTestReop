import os
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from github_webhook import Webhook
from flask import Flask, request, Response

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) 
gitToken = os.environ['GITTOKEN']
g = Github(gitToken)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)
