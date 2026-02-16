import unittest
import requests
import json
import github_userinfo

#Test 1: Testing Program runs

class TestGitHubInfo(unittest.TestCase):
    
    def test_github_userinfo_runs(self):
        user = "richkempinski"
        github_userinfo.showGithubInfo(user)
        self.assertTrue(True)

# Test 2: Test if the user has any repositories
    def test_userrepos(self):
        user = "richkempinski"
        url = "https://api.github.com/users/" + user + "/repos"
        response = requests.get(url)
        repos = json.loads(response.text)
        self.assertIsInstance(repos,list)
        self.assertGreater(len(repos),0)

#Test 3: Test if the user has commits
    def test_usercommits(self):
        user = "richkempinski"
        repo = "hellogitworld"

        url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
        response = requests.get(url)

        commits = json.loads(response.text)

        self.assertIsInstance(commits, list)
        self.assertGreaterEqual(len(commits), 0)

    

