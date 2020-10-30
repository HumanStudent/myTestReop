import os
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from github_webhook import Webhook
from flask import Flask, request, Response

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) 
gitToken = os.environ['GITTOKEN']
g = Github(gitToken)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)
