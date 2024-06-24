from github import Github
import os

token = os.getenv('GITHUB_TOKEN')
repo = os.getenv('GITHUB_REPOSITORY')

repository_full_name = f"surendba/{repo}"

g = Github(token)

repo = g.get_repo(repository_full_name)

open_issues = repo.get_issues(state='open')

for issue in open_issues:
    print(f"Issue #{issue.number}: {issue.title}")