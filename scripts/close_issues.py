import requests
import os

token = os.getenv('GITHUB_TOKEN')
repo = os.getenv('GITHUB_REPOSITORY')

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
            close_url = f"{url}/{issue_number}"
            data = {"state": "closed"}
            close_respose = requests.patch(close_url, headers=headers, json=data=)
            if close_respose.status_code == 200:
                print(f"Issue #{issue_number} is closed.")
            else
                print(f"Failed to close issue #{issue_number}.")


if __name__ == "__main__":
    close_issues()
