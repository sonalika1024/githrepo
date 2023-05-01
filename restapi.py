import requests

# set the owner and name of the repository
owner = 'OWNER'
repo = 'REPO'

# set the access token
access_token = 'YOUR_ACCESS_TOKEN'

# make a GET request to the GitHub REST API to get the language information
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/languages', headers=headers)

# parse the JSON response
languages = response.json()

# print the language information
for language, size in languages.items():
    print(f"{language}: {size} bytes")
