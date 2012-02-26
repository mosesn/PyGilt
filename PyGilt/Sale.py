from Image import Image

class Sale(object):
    def __init__(self, name, sale, sale_key, store, sale_url, begins,
                 image_urls, description="", ends="", product_urls=[]):
        self.name = name
        self.sale = sale
        self.sale_key = sale_key
        self.store = store
        self.sale_url = sale_url
        self.begins = begins
        self.images = [Image(img["url"], img["width"], img["height"])
                           for img_lst in image_urls.values()
                           for img in img_lst]
        self.description = description
        self.ends = ends
        self.product_urls = product_urls

def make_sale(smap):
    description = smap.get("description", "")
    ends = smap.get("ends", "")
    product_urls = smap.get("products", [])
    return Sale(smap["name"], smap["sale"], smap["sale_key"],
                smap["store"], smap["sale_url"], smap["begins"],
                smap["image_urls"], description=description, ends=ends,
                product_urls=product_urls)
