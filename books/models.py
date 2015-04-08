from django.db import models

import urllib2 as urllib
from PIL import Image
import io

import isbn_search

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name,)

class BookManager(models.Manager):
	def create_book(self, isbn):
		# get ISBN from amazon
		product = isbn_search.search_isbn(isbn)
		if product is None:
			return None
		book = self.create(
				isbn    = product.isbn,
				eisbn   = product.eisbn,
				author  = product.author,
				title   = product.title,
				edition = product.edition,
				)
		if product.cover_url is not '':
			cover_img_bin = urllib.urlopen(product.cover_url)
			cover_img_file = Image.open(io.BytesIO(cover_img_bin.read()))
			book.cover_img.save("cover.jpg", cover_img_file)
		return book

def upload_path(book, filename):
	return 'covers/%s/%s' % (book.isbn, filename)

class Book(models.Model):
	isbn = models.CharField(max_length=10, unique=True)
	eisbn = models.CharField(max_length=13, blank=True, null=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	edition = models.CharField(max_length=200, blank=True, null=True)
	cover_img = models.ImageField(upload_to=upload_path)
	def __unicode__(self):
		return u'[%s] "%s" by %s' % (self.isbn, self.title, self.author,)
	objects = BookManager()


class Book_copy(models.Model):
	book = models.ForeignKey(Book)
	owner = models.ForeignKey(User)
	purchase_date = models.DateTimeField('date published')
	def __unicode__(self):
		return u'%s borrowed by %s' % (self.book, self.owner,)

class Borrowing(models.Model):
	book_copy = models.ForeignKey(Book_copy)
	borrower = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s loaned by %s since %s' % (self.book_copy.book, self.borrower, self.borrow_date,)

