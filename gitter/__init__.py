import requests
from datetime import datetime

#Requests with no User-Agent header will be rejected.
#If you provide an invalid User-Agent header, you will receive a 403 Forbidden response.
user_agent = "gitter_app"

#The most common media types supported by the GitHub REST API are application/vnd.github+json and application/json.
headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}

def get_octocat():
  '''
  Get request to GitHub Octocat API endpoint. If successfull, return the Octocat.
  '''
  url = f"https://api.github.com/octocat"
  response = requests.get(url, headers=headers)
  
  if response.status_code == 200:
    return response.text
  else:
    return f"Request get_octocat failed with status code {response.status_code}"

def get_commits_today(username):
    '''
    Get request to the "users/{str: username}/events/public" API endpoint. Takes in the username as an
    argument and creates a date timestamp. If the repsonse has a length, return the length of the response.
    If no commits for the day, return an error message.
    '''
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url, headers=headers)
    date = datetime.now().isoformat()

    if response.status_code == 200:
        data = response.json()
        commits = [event['created_at'] for event in data if event['type'] == 'PushEvent' and event['created_at'].startswith(date[:10])]
        
        if commits is not None:
          return len(commits)
        else:
          return 0
        
    else:
        return f"Request failed with status code {response.status_code}"