from requests import get

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8080/api"

get_response = get(endpoint, params={"product_id":1}, json={"query":"hello"})
print(get_response.json())