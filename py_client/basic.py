from requests import get

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8080"

get_response = get(endpoint)
print(get_response.text)