from Image import Image

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
