import requests

# The API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make a GET request to the API
response = requests.get(url)

# Print the response in JSON format
print(response.json())
