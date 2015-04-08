import os, sys, inspect

import ConfigParser

import isbn_search

config_books = None

def init_config():
	global config_books
	try:
		cfg_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0],"../books.cfg")))
		config_books = ConfigParser.ConfigParser()
		config_books.read(cfg_path)
	except:
		print "Can not open config file %s" % cfg_path
		raise

init_config()
isbn_search.init_isbn(config_books)
