import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

# The API returns a response, which can be converted to JSON
data = response.json()

# You can then interact with this data as a regular Python dictionary
for post in data:
    print(post['title'])