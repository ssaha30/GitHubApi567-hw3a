import requests
import json

def githubrepo(user):

    # Get user's repositories
    repos_url = "https://api.github.com/users/" + user + "/repos"
    repos_response = requests.get(repos_url)
    repos = json.loads(repos_response.text)

    if type(repos)==dict:
        print("Invalid username")
        return

    # Go through each repository
    for repo in repos:

        if "name" not in repo:
            continue

        repo_name = repo["name"]

        # Get commits for this repo
        commits_url = "https://api.github.com/repos/" + user + "/" + repo_name + "/commits"
        commits_response = requests.get(commits_url)
        commits = json.loads(commits_response.text)

        
        print("Repo:", repo_name, "Number of commits:", len(commits))

def main():

    user = input("Enter GitHub Username: ")
    githubrepo(user)

if __name__ == "__main__":
    main()


