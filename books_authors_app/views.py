from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect


# Create your views here.
def books(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": authors.objects.all()
    }
    return render(request, "book.html", context)

def author(request):
    context = {
    "all_the_authors": authors.objects.all(),
    "all_the_books": Book.objects.all()
    }
    return render(request, "author.html", context)
# # render just brings up
# -------------------------------------------------
def process(request):


    # since we are trying to update  here is the template we should follow

    # c = ClassName.objects.get(id=1)
    # c.field_name = "some new value for field_name"
    # c.save()

    # grab the book to add
    id_from_form = request.POST["book_selected"]
    book_from_database = Book.objects.get( id = id_from_form )
    # grab the author we want to add the book to 
    author_id_from_form = authors.objects.get(id = request.POST["author_from_form"])
    # assign book to the author, (which author?)
    book_from_database.publishers.add(author_id_from_form)

    book_from_database.save()


    # print(request.POST['book_selected'])
    # id_from_form = request.POST['book_selected']
    # book_from_database = Book.objects.get(id = id_from_form )
    # [print(book_from_database)]
    return  redirect('/details/'+request.POST["author_from_form"])
# -----------------------------------------------
def creating_book(request):
    # request.post is calling by key name
    # form is empty dict waiting to be sent to server
    Book.objects.create(title=request.POST["title"], desc=request.POST["desc"])
    return  redirect ('/thanku')

def creating_author(request):
    # request.post is calling by key name
    # form is empty dict waiting to be sent to server
    authors.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"] )
    return  redirect ('/thanku')
# for many to many relationships you don"t need the following, you can add it in later via terminal
# books=Book.objects.get(id=request.POST["books"])
def thanku(request):

    return render (request, "thanku.html")

# def creating_ninjas(request):
#     Ninjas.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],dojo_visited=Dojo.objects.get(id=request.POST["dojo_visited"]))
#     return  redirect ('/thanku')
# #  so the dojo_visited is the foregn key which is set to the id entered by the user (option button) refer to dojo.html

# # ["kfdkg"] = key name
def details(request,id_from_route):
    # we need some way to capture id from front end when someone clicks
    details = authors.objects.get(id=id_from_route)
    context ={
        "all_the_books": Book.objects.all(),
        'one_author' : details,
    }
    return render(request,'details.html', context)