from requests import get

from Product import make_product

from Sale import make_sale

from json import loads

class GiltClient:
    def __init__(self, key):
        self.query = {"apikey" : key}
        self.stores = set(["women", "men", "kids", "home"])

    def active(self, store_key = ""):
        if store_key:
            if store_key in self.stores:
                uri = "https://api.gilt.com/v1/sales/" + store_key + "/active.json"
        else:
            uri = "https://api.gilt.com/v1/sales/active.json"
        resp = get(uri, params=self.query)
        return [make_sale(x) for x in loads(resp.text)["sales"]]

    def upcoming(self, store_key = ""):
        if store_key:
            if store_key in self.stores:
                uri = "https://api.gilt.com/v1/sales/" + store_key + "/upcoming.json"
        else:
            uri = "https://api.gilt.com/v1/sales/upcoming.json"
        resp = get(uri, params=self.query)
        return [make_sale(x) for x in loads(resp.text)["sales"]]

    def sale_detail(self, store_key, sale_key):
        uri = "https://api.gilt.com/v1/sales/" + store_key + "/" + sale_key + "/detail.json"
        resp = get(uri, params=self.query)
        return make_sale(loads(resp.text))

    def product_detail(self, product_id):
        start = "https://api.gilt.com/v1/products/"
        if len(product_id) > len(start):
            uri = product_id
        else:
            uri = start + product_id + "/detail.json"
        resp = get(uri, params=self.query)
        return make_product(loads(resp.text))
