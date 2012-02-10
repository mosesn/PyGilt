from requests import get

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

class Image:
    def __init__(self, url, width, height):
        self.url = url
        self.width = width
        self.height = height

class SKU:
    def __init__(self, sku_id, inventory_status, msrp_price, sale_price,
                 shipping_surcharge="", attributes=[]):
        self.id = sku_id
        self.inventory_status = inventory_status
        self.msrp_price = msrp_price
        self.sale_price = sale_price
        if shipping_surcharge:
            self.shipping_surcharge = shipping_surcharge
        if attributes:
            self.attributes = dict([(attr["name"], attr["value"]) for attr in attributes])

def make_sku(smap):
    shipping_surcharge = smap.get("shipping_surcharge", "")
    attributes = smap.get("attributes", [])
    return SKU(smap["id"], smap["inventory_status"], smap["msrp_price"],
               smap["sale_price"], shipping_surcharge, attributes)

class Product:
    def __init__(self, name, product, product_id, brand, url, image_urls,
                 skus, description="", fit_notes="", material="",
                 care_instructions="", origin=""):
        self.name = name
        self.product = product
        self.product_id = product_id
        self.brand = brand
        self.url = url
        self.image_urls = [Image(img["url"], img["width"], img["height"])
                           for img_lst in image_urls.values()
                           for img in img_lst]
        self.skus = [make_sku(sku) for sku in skus]
        if description:
            self.description = description
        if fit_notes:
            self.fit_notes = fit_notes
        if material:
            self.material = material
        if care_instructions:
            self.care_instructions = care_instructions
        if origin:
            self.origin = origin

def make_product(pmap):
    description = pmap.get("description", "")
    fit_notes = pmap.get("fit_notes", "")
    material = pmap.get("material", "")
    care_instructions = pmap.get("care_instructions", "")
    origin = pmap.get("origin", "")
    return Product(pmap["name"], pmap["product"], pmap["id"], pmap["brand"],
                   pmap["url"], pmap["image_urls"], pmap["skus"], description,
                   fit_notes, material, care_instructions, origin)

class Sale:
    def __init__(self, name, sale, sale_key, store, sale_url, begins,
                 image_urls, description="", ends="", products=[]):
        self.name = name
        self.sale = sale
        self.sale_key = sale_key
        self.store = store
        self.sale_url = sale_url
        self.begins = begins
        self.image_urls = [Image(img["url"], img["width"], img["height"])
                           for img_lst in image_urls.values()
                           for img in img_lst]
        if description:
            self.description = description
        if ends:
            self.ends = ends
        if products:
            self.products = products

def make_sale(smap):
    description = smap.get("description", "")
    ends = smap.get("ends", "")
    products = smap.get("products", [])
    return Sale(smap["name"], smap["sale"], smap["sale_key"],
                smap["store"], smap["sale_url"], smap["begins"],
                smap["image_urls"], description=description, ends=ends,
                products=products)
