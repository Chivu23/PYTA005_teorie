import requests

class ProductsApi:

    __BASE_URL = "https://dummyjson.com/products"

    def get_products(self):
        response = requests.get(self.__BASE_URL)
        return response

    def
