from pprint import pprint

stock = [
    {"name": "iphone 12", "stock": 24, "price": 65432.1,
       "recomended": ["Samsung Galaxy S21", "iphone12"]},
    {"name": "Samsung Galaxy S21", "stock": 8, "price": 50000.0, "discount": 5000},
    {"name": "Xiaomi Mi10t lite", "stock": 42, "price": 35000.5} 
]

print(type(stock))
print(type(stock[0]))
print(type(stock[0]["recomended"]))