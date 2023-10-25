import requests
import json

product_id = input("Enter the id: ")

try:
    product_id = int(product_id)
except:
    print(f"{product_id} is not a valid id")
    product_id = None

title = input("Enter the new title: ")
price = input("Enter the new price: ")
content = input("Enter the new content: ")

data = {
    'title': title,
    'content': content,
}

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/update"
    headers = {'Content-Type': 'application/json'}  # Specify the content type as JSON
    put_response = requests.put(endpoint, data=json.dumps(data), headers=headers)

    if put_response.status_code == 200:
        print("Update successful")
    else:
        print("Update failed")
    