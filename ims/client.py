import requests


url = 'http://127.0.0.1:8000/api/stock/auth/'
#headers = {'Authorization': 'Token 50944de40baf794efb4a5d549d28935058195152'}
# r = requests.get(url, headers=headers)
# print(r.json())
# url = "http://127.0.0.1:8000/api/stock/products"
response = requests.get(url)
# print(response.text)
# url = "http://127.0.0.1:8000/api/stock/products/"
#
# response = requests.get(url)
# print(response.text)
# import sys, json
def get_token():
    url = "http://127.0.0.1:8000/api/stock/auth"
#
    response = requests.post(url, data={'username': 'udit',
                                         'password': '1234'})
#
    return response.json()
#
# get_token()





def get_data():
     url = "http://127.0.0.1:8000/api/stock/products"
     header = {'Authorization': 'Token 50944de40baf794efb4a5d549d28935058195152'}
     response = requests.get(url, headers=header)
     print(response.text)


def create_new():
    url = "http://127.0.0.1:8000/api/stock/products/"
    header = {'Authorization': 'Token 50944de40baf794efb4a5d549d28935058195152'}
    data ={
        "id": 1,
        "category": "Grocery",
        "price": 6,
        "item_name": "wheat",
        "quantity": 7,
        "receive_quantity": 0,
        "receive_by": 'null',
        "issue_to": 'null',
        "phone_number": 'null',
        "created_by": 'null',
        "reorder_level": 0,
        "last_updated": "2020-12-01T17:11:36.658180Z",
        "timestamp": "2020-12-01T17:11:36.658180Z",
        "export_to_CSV": 'false'
    }
    response = requests.post(url, data=data , headers=header)
    print(response.text)

def edit_data(id):
    url = f"http://127.0.0.1:8000/api/stock/{id}/update"
    header = {'Authorization': 'Token 50944de40baf794efb4a5d549d28935058195152'}
    data ={
    "category": "Stationary",
    "price":7,
    }
    response = requests.put(url, data=data , headers=header)
    print(response.text)



def delete_data(id):
    url = f"http://127.0.0.1:8000/api/stock/{id}/update"
    header = {'Authorization': 'Token 50944de40baf794efb4a5d549d28935058195152'}

    response = requests.delete(url,headers=header)
    print(response.text)

delete_data(5)
