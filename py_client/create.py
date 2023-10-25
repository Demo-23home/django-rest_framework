import requests

headers = {'Authorization': 'Bearer913356f03a8302b11c92013a4373b066b2a3a426'}


endpoint = "http://localhost:8000/api/products/"    


data = {
    "title":"This filed is done",
    "price":120
}


get_response = requests.post(endpoint, json=data, headers=headers)


print(get_response.json())