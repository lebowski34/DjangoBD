from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *

def paginated_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "posts.html", {'page_obj': page_obj})

def sign_up_by_django(request):
    buyers = Buyer.objects.values_list("name", flat=1)
    print(list(buyers))
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in list(buyers):
                error = "Пользователь уже существует"
                info = {
                    'error': error
                }
                return render(request, "registration_page.html", info)
            if password != repeat_password:
                error = "Пароли не совпадают"
                info = {
                    'error': error
                }
                return render(request, "registration_page.html", info)
            if int(age) <= 17:
                error = "Возраст должен быть 18+"
                info = {
                    'error': error
                }
                return render(request, "registration_page.html", info)
            Buyer.objects.create(name=username, balance='0', age=age)
            return HttpResponse(f"Добро пожаловать, {username}")
    else:
        form = UserRegister()
    return render(request, "registration_page.html", {'form': form})


class menu(TemplateView):
    template_name = 'menu.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context

class cart_temp(TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Корзина'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context

class games_temp(TemplateView):
    template_name = 'games.html'
    def get_context_data(self, **kwargs):
        games = Game.objects.all()
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Игры'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        context['games'] = games
        return context

class platform_temp(TemplateView):
    template_name = 'platform.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context