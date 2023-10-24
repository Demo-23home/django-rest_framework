import requests



endpoint = "http://localhost:8000/api/products/"    


data = {
    "title":"This filed is done",
    "price":120
}


get_response = requests.post(endpoint,json=data)


print(get_response.json())