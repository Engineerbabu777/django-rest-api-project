from requests import get

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api"

get_response = get(endpoint)
print(get_response.json())