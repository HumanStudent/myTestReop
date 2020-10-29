import os
from github import Github
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) 
gitToken = os.environ['GITTOKEN']
g = Github(gitToken)
# GITHUB_ACCESS_TOKEN
# g = Github("HumanStudent", "hellohuman1")

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)
