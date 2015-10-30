#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jreybert <jreybert@dionysos.lin.mbt.kalray.eu>
#
# Distributed under terms of the MIT license.

"""
ISBN search module (can only search on amazon AWS for the moment)
"""

from StringIO import StringIO
import urllib
#from PIL import Image

import os, sys, inspect
package_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"lib","python2.7","site-packages")))
if package_subfolder not in sys.path:
	 sys.path.insert(0, package_subfolder)
from amazon.api import AmazonAPI

amazon_conn = None

def init_amazon(config):
	global amazon_conn
	try:
		amazon_conn = AmazonAPI(
			config.get('amazon', 'access_key'),
			config.get('amazon', 'secret_key'),
			config.get('amazon', 'associate_tag'),
			region=config.get('amazon', 'locale')
			)
	except:
		print "Can not open amazon"
		raise
	if amazon_conn == None:
		raise "Can not open amazon"

def init_isbn(config):
	init_amazon(config)

def search_amazon(isbn):
	try:
		product = amazon_conn.lookup(ItemId=isbn)
	except:
		print "ISBN '%s' not found on amazon" % (isbn)
		return None
	return ISBN_product(product)

def search_isbn(isbn):
	return search_amazon(isbn)

class ISBN_product(object):
	"""
	A wrapper class for object found
	"""

	def __init__(self, amazon_prod):
		self.isbn             = amazon_prod.isbn
		self.eisbn            = amazon_prod.eisbn
		self.title            = amazon_prod.title
		self.author           = amazon_prod.author
		self.edition          = amazon_prod.edition
		self.publication_date = amazon_prod.publication_date
		self.release_date     = amazon_prod.release_date
		self.cover_url        = amazon_prod.medium_image_url


