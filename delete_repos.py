import requests

def delete_repos(team_name, repo_prefix):
    # Get the repositories in the team
    repositories = get_team_repositories(team_name)
    
    # Iterate over the repositories
    for repository in repositories:
        # Check if the repository name starts with the specified prefix
        if repository.startswith(repo_prefix):
            # Delete the repository
            delete_repository(repository)

def get_team_repositories(team_name):
    url = f"https://api.github.com/orgs/{team_name}/repos"
    headers = {"Authorization": f"Bearer {YOUR_GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [repo["name"] for repo in response.json()]

def delete_repository(repository):
    url = f"https://api.github.com/repos/{repository}"
    headers = {"Authorization": f"Bearer {YOUR_GITHUB_TOKEN}"}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    print(f"Deleted repository: {repository}")

# Define the GitHub team and repository prefix
team_name = "your-team-name"
repo_prefix = "zzz-"

# Call the delete_repos function
delete_repos(team_name, repo_prefix)