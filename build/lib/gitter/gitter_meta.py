import requests

user_agent = "gitter_app"
#User-Agent: Awesome-Octocat-App
#Requests with no User-Agent header will be rejected.

headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
#If you provide an invalid User-Agent header, you will receive a 403 Forbidden response.
#The most common media types supported by the GitHub REST API are application/vnd.github+json and application/json.

def get_octocat():
  api_url = "https://api.github.com/octocat"
  response = requests.get(api_url, headers=headers)
  return {"text": response.text, "status": response.status_code}