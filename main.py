import requests
import json


def switch(choice):

    if choice == "1":
        data=place_order()
        print("Order placed successfully and your order id is ",data['orderId'])
        print("your order status is ",data['orderStatus'])

    elif choice == "2":
        orderid=input("Enter the order id for modification of your order")
        data=order_modification(orderid)
        print("your order is successfully modified with order id ",data['orderId'])
        print("your order status is ",data['orderStatus'])
        
    elif choice == "3":
        orderid=input("enter the order id to cancel the order")
        data=order_cancellation(orderid)
        print("your order status of order id ",data['orderId']," and the status of your order is ", data['orderStatus'])

    elif choice == "4":
        data=order_book()
        print(data)
    elif choice == "5": 
        orderid=input("enter the order id to cancel the order")
        get_order_by_id(orderid)

    

def place_order():
    url = "https://api.dhan.co/orders"
    payload = json.dumps({
    "dhanClientId": "1000000003",
    "correlationId": "123abc678",
    "transactionType": "BUY",
    "exchangeSegment": "NSE_EQ",
    "productType": "INTRADAY",
    "orderType": "MARKET",
    "validity": "DAY",
    "tradingSymbol": "",
    "securityId": "11536",
    "quantity": "5",
    "disclosedQuantity": "",
    "price": "3424.80",
    "triggerPrice": "",
    "afterMarketOrder":False,
    "amoTime": "",
    "boProfitValue": "",
    "boStopLossValue": "",
    "drvExpiryDate": "string",
    "drvOptionType": "CALL",
    "drvStrikePrice": -3.402823669209385e+38
    })

    headers = {
    'Content-Type': 'application/json',
    'access_token':'JWT'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    print(response.status_code)
    print(data['orderId'])
    print(data['orderStatus'])
    return data


def order_modification(orderid):
    
    url="https://api.dhan.co/orders/"+orderid
    payload = json.dumps({
   "dhanClientId": "string",
   "orderId": orderid,
   "orderType": "LIMIT",
   "legName": "ENTRY_LEG",
   "quantity": "40",
   "price": "3345.8",
   "disclosedQuantity": "10",
   "triggerPrice": "",
   "validity": "DAY"
  })

    headers = {
    'Content-Type': 'application/json',
    'access_token':'JWT'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    data = response.json()
    print(data['orderId'])
    print(data['orderStatus'])
    return data
def order_cancellation(orderid):
    url='https://api.dhan.co/orders/'+orderid
    headers = {
    'Content-Type': 'application/json',
    'access_token':'JWT'
    }
    response = requests.request("DELETE", url, headers=headers)
    # print request object
    print(response.url)
  
    # print status code
    print(response.status_code)
    
    data = response.json()
    print(data['orderId'])
    print(data['orderStatus'])
    return data

def order_book():
    url='https://api.dhan.co/orders/'
    headers = {
    'Content-Type': 'application/json',
    'access_token':'JWT'
    }
    response = requests.request("GET", url, headers=headers)
    
    data = response.json()
    return data


def get_order_by_id(orderid):
    url='https://api.dhan.co/orders/'+orderid
    headers = {
    'Content-Type': 'application/json',
    'access_token':'JWT'
    }
    response = requests.request("GET", url, headers=headers)
    
    data = response.json()
    return data



def main():
    while 1:
        a = input("Enter 1 to Place order, Enter 2 to modify order, Enter 3 to cancel order, Enter 4 to check all orders, Enter 5 to get the order by id ")
        b=int(a)
        if b >5 or b < 0:
            return 0    
        else:    
            switch(a)
        
main()