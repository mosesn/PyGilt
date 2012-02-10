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
