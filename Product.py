from Image import Image

from SKU import make_sku

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

