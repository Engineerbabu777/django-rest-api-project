from requests import get,post

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api/products/1/"

get_response = get(endpoint)
print(get_response.json())