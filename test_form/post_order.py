import requests

if __name__ == "__main__":
    session = requests.Session()
    data = {
        "table": 1,
        "list": [{"id": 1, "name": "pork", "count": 1, "price": 20}, {"id": 2, "name": "fish", "count": 1, "price": 23}]
    }
    print("data", data)
    r = session.post("http://127.0.0.1:5000/api/test_order", data = data)
    print("r", r)