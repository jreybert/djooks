from django.db import models

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name,)

class Book(models.Model):
	isbn = models.CharField(max_length=10, unique=True)
	eisbn = models.CharField(max_length=13, unique=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	edition = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='covers')
	def __unicode__(self):
		return '[%s] "%s" by %s' % (self.isbn, self.title, self.author,)

	@classmethod
	def create(cls, isbn):
		book = cls(isbn=isbn)
		return book


class Book_copy(models.Model):
	book = models.ForeignKey(Book) 
	owner = models.ForeignKey(User)
	purchase_date = models.DateTimeField('date published')
	def __unicode__(self):
		return '%s borrowed by %s' % (self.book, self.owner,)

class Borrowing(models.Model):
	book_copy = models.ForeignKey(Book_copy)
	borrower = models.ForeignKey(User)
	borrow_date = models.DateTimeField('date published')
	def __unicode__(self):
		return '%s loaned by %s since %s' % (self.book_copy.book, self.borrower, self.borrow_date,)

