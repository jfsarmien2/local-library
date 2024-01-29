from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, BookInstance, Author, Genre
# Create your views here.


def index(request):

    num_of_books = Book.objects.all().count()
    num_of_instance = BookInstance.objects.all().count()

    num_of_instance_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_of_authors = Author.objects.count()

    context = {
        'num_books': num_of_books,
        'num_instances': num_of_instance,
        'num_instances_available': num_of_instance_available,
        'num_authors': num_of_authors,
    }

    return render(request, 'index.html', context)


class BookListView(ListView):
    model = Book
    paginate_by = 2


class BookDetailView(DetailView):
    model = Book
