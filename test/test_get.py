import unittest
from PyGilt.GiltClient import GiltClient
from os import getenv

class TestGet(unittest.TestCase):
   def setUp(self):
      # !!! get this from an environment variable !!
      api_key = getenv("GILTAPIKEY")
      if api_key == None:
         raise Exception("Set the environment variable GILTAPIKEY to your API key")
      self.giltClient = GiltClient(api_key)

   def test_get_active_sale(self):
      active_sales = self.giltClient.active("men")
      sale = active_sales[0]
      # print "Found Sale name = %s" % sale.name
      self.assertTrue(len(sale.name) > 5)

   def test_get_product(self):
      active_sales = self.giltClient.active("women")
      sale = active_sales[0]
      product_url = sale.product_urls[0]
      product = self.giltClient.product_detail(product_url)
      # print "Found Product name = %s" % product.name
      self.assertTrue(len(product.name) > 5)

   def test_product_image(self):
      active_sales = self.giltClient.active("kids")
      sale = active_sales[0]
      product_url = sale.product_urls[0]
      product = self.giltClient.product_detail(product_url)
      image = product.images[0]
      # print "Found Product image = %s" % image.url
      self.assertTrue(image.width > 10)

"""

active_sales = giltClient.active("men")

for sale in active_sales:
   print sale.name
   print sale.products
   product_uris = sale.products
   for product_uri in product_uris:
      print "product URI is %s" % product_uri
      product = giltClient.product_detail(product_uri)
      for image in product.image_urls:
         print "image url %s" % image.url
         print "image width %d" % image.width
      print "product name is %s" % product.name
"""
