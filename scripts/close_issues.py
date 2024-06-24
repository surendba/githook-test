import requests
import os

token = os.getenv('GITHUB_TOKEN')
repo = os. environ('GITHUB_REPOSITORY')

url =f"https://api.github.com/repos/{repo}/issues"

headers = {
    "authorization" : f"token {token}",
    "Accept" : "application/vnd.github.v3+json"
}

def close_issues():
    
    params = {"state" : "open"}
    response = requests.get(url, headers=headers, params=params)
    issues = response.json()

    for issue in issues:
        if "pull_request" not in issue:
            issue_number = issue["number"]


if __name__ == "__main__":
    close_issues()
