import requests




get_product_id = input("what is the Product id for which you want to delete? : ")

try :
    get_product_id = int(get_product_id)
except:
    get_product_id = None
    print(f"{get_product_id} is not a valid Product id")



if get_product_id: 
    endpoint = f'http://localhost:8000/api/products/{get_product_id}/delete/'
    get_response = requests.delete(endpoint)
    print(get_response.json())
