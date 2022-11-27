from django.shortcuts import render , redirect , get_object_or_404 
from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        add_book = AddBookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    if request.method == 'POST':
        add_category = AddCategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
    'books': Book.objects.all(),
    'category': Category.objects.all(),
    'addbook' : AddBookForm(),
    'addcategory' : AddCategoryForm(),
    'allbooks' : Book.objects.filter(active=True ).count(),
    'allsoldbooks' : Book.objects.filter(status='sold').count(),
    'allrantalbooks' : Book.objects.filter(status='rental').count(),
    'allavaliblebooks' : Book.objects.filter(status='availble').count(),

}
    return render(request ,'pages/index.html', context)
def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:  
            search = search.filter(title__icontains=title )          
    
    context = {
    'books': search ,
    'addcategory' : AddCategoryForm(),
    'category': Category.objects.all(),
    'allbooks' : Book.objects.filter(active=True ).count(),
    'allsoldbooks' : Book.objects.filter(status='sold').count(),
    'allrantalbooks' : Book.objects.filter(status='rental').count(),
    'allavaliblebooks' : Book.objects.filter(status='availble').count(),


}
    return render(request , 'pages/books.html' , context)

def update(request , id):
    book_id = Book.objects.get(id= id)
    if request.method == 'POST':
        book_save = AddBookForm(request.POST , request.FILES , instance=book_id)
        if book_save.is_valid:
            book_save.save()
            return redirect('/')

    else:
        book_save = AddBookForm(instance= book_id)
    context = {
        'form' : book_save
    }
    return render(request, 'pages/update.html' , context)

def delete(request , id):
    book_id_delete = get_object_or_404(Book , id=id)
    if request.method == 'POST':
        book_id_delete.delete()
        return redirect('/')
    return render(request , 'pages/delete.html')