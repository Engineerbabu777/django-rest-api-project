from requests import get,post

# endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"This field is ok",
    "price":56
}
get_response = get(endpoint)
print(get_response.json())