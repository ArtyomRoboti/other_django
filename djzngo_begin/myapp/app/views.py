from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
# def index(request):
#     name = request.GET.get('name', 'Guest')
#     age = request.GET.get('age', '0')
#     return HttpResponse(f'Hello, {name} {age}')
#
#
# def simple_post(request):
#     if request.method == 'POST':
#         message = request.POST.get('message', '')
#         return HttpResponse(f'You said: {message}')
#     return render(request, 'index2.html')
#
#
#
# С помощью HTTP запрпосов создание формы
# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe') == 'on'
#
#         print(f'Name: {name}')
#         print(f'Email: {email}')
#         print(f'Message: {message}')
#         print(f'Subscribe: {subscribe}')
#
#         return HttpResponse('Форма была отправлена успешно')
#
#     return render(request, 'index.html')

# С помощью классов Django создание формы
# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             subscribe = form.cleaned_data['subscribe']
#     else:
#         form = ContactForm()
#     return render(request, 'index.html', {'form': form})




# def index(request):
#     Authors = Author.objects.all()
#     context = {
#         'Authors': Authors,
#     }
#     return render(request, 'index.html', context)
#
# def test(request):
#     context = {
#         'a':1
#     }
#     return render(request, 'test.html', context)

def index(request):
    if request.method == 'POST':
        number_title = request.POST.get('list_title')
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, int(number_title))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj' : page_obj})