from github import Github
from pathlib import Path
from dotenv import load_dotenv

# env_path = Path('.') / '.varFileEnv'
# load_dotenv(dotenv_path=env_path) 
g = Github("cf917c4077d34dedf75401ef5e5fef548aa7a1f0")
# GITHUB_ACCESS_TOKEN
# g = Github("HumanStudent", "hellohuman1")

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)
