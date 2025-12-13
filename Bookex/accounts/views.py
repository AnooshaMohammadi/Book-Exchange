# account/views.py
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Book,Exchange,User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .user_form import UserRegistrationForm
from django.contrib import messages
from .login_form import LoginForm
from .models import User
#from django.contrib.auth.models import Session
from .book_form import BookForm
from django.utils import timezone
from django.db.models import Q


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('user_login')  # Replace 'login' with the actual name of your login view
        return render(request, self.template_name, {'form': form })


def login_page(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                #username = form.cleaned_data['username']
                m = User.objects.get(username=request.POST["username"])
                request.session["member_id"] = m.id
                return redirect('home')
            else:
                messages.error(request, "login failed")
    return render(
        request, 'login.html', context={'form': form, 'message': messages})


def log_out(request):
    logout(request)
    return render(request,'startpage.html')

def say_hi(request):
    return render(request, 'base.html')


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})


def profile(request):
    userid = request.session.get('member_id')
    member = get_object_or_404(User, pk=userid)
    return render(request, 'profile.html', {'user': member})


class home(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'

def startpage(request):
    return render(request, 'startpage.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the owner of the book to the current logged-in user
            form.instance.owner = request.user
            form.save()
            return redirect('add_book')  # Replace 'book_list' with the actual URL name for listing books
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


class my_books(ListView):
    model = Book
    template_name = 'my_books.html'


def exchange(request, book_id):


    book = get_object_or_404(Book, pk=book_id)
    userid = request.session.get('member_id')
    m = User.objects.get(id=userid)
    exchange = Exchange(thebook=book, borrower=m, lender=book.owner, status="pending",date=timezone.now())
    exchange.save()
    return redirect('home')


class request_history(ListView):
    model = Exchange
    template_name = 'request_history.html'

def accept(request, ex_id):

    Exchange.objects.filter(id=ex_id).update(status="accepted")

    return render(request,'profile.html')

def phone(request,username):
    user = get_object_or_404(User, username=username)
    phone_number = user.phonenumber
    return HttpResponse(phone_number)