from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Book ID is {self.id} : and title is {self.title}>'

class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Author ID is {self.id}: {self.first_name}>'

# this_book = Book.objects.get(id=4)	# retrieve an instance of a book
# this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
    
# # 2 options that do the same thing:
# this_publisher.books.add(this_book)		# add the book to this publisher's list of books
# # OR
# this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers
# <div id="copy-toolbar-container" style="cursor: pointer; position: absolute; top: 5px; right: 5px; padding: 0px 3px; background: rgba(224, 224, 224, 0.2) none repeat scroll 0% 0%; box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; color: rgb(187, 187, 187); border-radius: 0.5em; font-size: 0.8em;"><span id="copy-toolbar">copy</span></div>