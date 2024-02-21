import requests
from datetime import datetime, timedelta

user_agent = "gitter_app"
#User-Agent: Awesome-Octocat-App
#Requests with no User-Agent header will be rejected.

headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
#If you provide an invalid User-Agent header, you will receive a 403 Forbidden response.
#The most common media types supported by the GitHub REST API are application/vnd.github+json and application/json.

def get_octocat():
  url = f"https://api.github.com/octocat"
  response = requests.get(url, headers=headers)
  return {"text": response.text, "status": response.status_code}

def get_commits_today(username):
    # Get the current date in the format required by GitHub API
    date = datetime.now().isoformat()

    # GitHub API url for the user's events
    url = f"https://api.github.com/users/{username}/events/public"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # If the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()

        # Filter the data to only include commit events from today
        commits = [event for event in data if event['type'] == 'PushEvent' and event['created_at'].startswith(date[:10])]

        return commits

    else:
        # If the request was not successful, print the status code and return None
        print(f"Request failed with status code {response.status_code}")
        return None

# # Replace 'username' with the GitHub username you're interested in
# commits = get_commits_today('akatheduelist')

# if commits is not None:
#     print(f"Found {len(commits)} commits today.")
# else:
#     print("No commits found today.")

