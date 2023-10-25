import requests


product_id = input(f"enter the id : ")


try:
    product_id = int(product_id)
except:
    print(f"{product_id} is not a valid id")
    product_id = None


if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}"
    get_response = requests.get(endpoint)
    print(get_response.json())
    

