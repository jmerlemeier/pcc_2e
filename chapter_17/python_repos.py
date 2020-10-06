import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} # Define Headers needed for the API call - we need GitHub Version 3
r = requests.get(url, headers=headers) #'r' will be the response object
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(response_dict.keys())

print(f"Total repos: {response_dict['total_count']}")

# # How many Repos in the Response Dictionary? 
repos = response_dict['items']
# print(f"Total items: {len(repos)}")

# First Repo Information
first_repo = repos[0]
# print(f"Keys: {len(first_repo)}")
# print(f"Below are the key names:")
# for key in sorted(first_repo.keys()):
#     print(key)

# for first_repo in repos:
#     print(f"Name: {first_repo['name']}")
#     print(f"URL: {first_repo['url']}")
#     print(f"Stargazers: {first_repo['stargazers_count']}")
#     print(f"Description: {first_repo['description']}")

url = 'https://api.github.com/rate_limit'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

response_dict = r.json()
for key in response_dict.keys():
    print(key)

print(f"Rate: {response_dict['rate']}")