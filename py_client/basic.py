from requests import get

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api"

get_response = get(endpoint, params={"abc":12}, json={"query":"hello"})
print(get_response.json())