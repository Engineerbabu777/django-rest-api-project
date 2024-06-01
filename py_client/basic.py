from requests import get,post

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8080/api/"

get_response = post(endpoint, params={"product_id":1}, json={"content":"hello","title":"title","price":32.0})
print(get_response.json())