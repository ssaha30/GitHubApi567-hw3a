import unittest
import json
from unittest import mock
import github_userinfo

#Fake Response
class MockResponse:
    def __init__(self,text):
        self.text = text
#Test 1: Testing Program runs

class TestGitHubInfo(unittest.TestCase):
    @mock.patch('requests.get')
    def test_github_userinfo_runs(self,mockedReq):
        mockedReq.return_value = MockResponse('[{"name":"repo1"},{"name":"repo2"}]')
        github_userinfo.githubrepo("richkempinski")
        self.assertTrue(True)

# Test 2: Test if the user has any repositories
    @mock.patch('requests.get')
    def test_userrepos(self,mockedReq):
        mockedReq.return_value = MockResponse('[{"name":"repo1"},{"name":"repo2"}]')
        response = mockedReq.return_value
        repos = json.loads(response.text)
        self.assertEqual(len(repos), 2)

#Test 3: Test if the user has commits
    @mock.patch('requests.get')
    def test_usercommits(self,mockedReq):
        mockedReq.side_effect = [
            MockResponse('[{"name":"repo1"}]'),
            MockResponse('[{"sha":1},{"sha":2},{"sha":3}]')]

        github_userinfo.githubrepo("richkempinski")
        self.assertTrue(True)

#Test 4: Test by inputting the user has putting 0 repos
    @mock.patch('requests.get')
    def test_forrepos(self, mockedReq):
        mockedReq.return_value = MockResponse('{"message":"Not Found"}')
        result = github_userinfo.githubrepo("baduser")
        self.assertIsNone(result)

        
 







#import unittest
#import requests
#import json
#import github_userinfo

#Test 1: Testing Program runs

#class TestGitHubInfo(unittest.TestCase):
    
 #   def test_github_userinfo_runs(self):
  #      user = "richkempinski"
   #     github_userinfo.githubrepo(user)
    #    self.assertTrue(True)

# Test 2: Test if the user has any repositories
    #def test_userrepos(self):
     #   user = "richkempinski"
      #  repos_url = "https://api.github.com/users/" + user + "/repos"
       # repos_response = requests.get(repos_url)
        #repos = json.loads(repos_response.text)
        #self.assertIsInstance(repos,list)
        #self.assertGreater(len(repos),0)

#Test 3: Test if the user has commits
    #def test_usercommits(self):
     #   user = "richkempinski"
      #  repo = "hellogitworld"

#        commits_url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
 #       commits_response = requests.get(commits_url)
#
 #       commits = json.loads(commits_response.text)
#
 #       self.assertIsInstance(commits, list)
  #      self.assertGreaterEqual(len(commits), 0)

#Test 4: Test by inputting the user has putting 0 repos
   # def test_forrepos(self):
    #    user = "richkempinski"
     #   url = "https://api.github.com/users/" + user + "/repos"
      #  response = requests.get(url)
       # repos = json.loads(response.text)
       # self.assertEqual(len(repos),0)
        
   

