from django.db import models

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name,)

class BookManager(models.Manager):
	def create_book(self, isbn):
		# get ISBN from amazon
		book = self.create(isbn=isbn)
		# do something with the book
		return book

class Book(models.Model):
	isbn = models.CharField(max_length=10, unique=True)
	eisbn = models.CharField(max_length=13, blank=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	edition = models.CharField(max_length=200, blank=True)
	cover = models.ImageField(upload_to='covers', blank=True)
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
	borrow_date = models.DateTimeField('date published')
	def __unicode__(self):
		return u'%s loaned by %s since %s' % (self.book_copy.book, self.borrower, self.borrow_date,)

