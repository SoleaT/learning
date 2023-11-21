import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.response import TemplateResponse
import logging
from django.utils import timezone
from faker import Faker
from myapp.forms import ProductForm, CategoryForm
from myapp.models import Product, Client, Order, Category, OrderDetail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

fake = Faker('ru-RU')
logger = logging.getLogger(__name__)
homeworks = [
    {'link': 'homework1', 'img_url': 'images/shop_01.jpg', 'name': 'про сайтик'},
    {'link': 'seminar2', 'img_url': 'images/shop_02.jpg', 'name': 'про бложек'},
    {'link': 'homework2', 'img_url': 'images/shop_03.jpg', 'name': 'про инет-магазин'},
]


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog')


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog')


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    # extra_context = {'admin_mode': True}
    template_name = 'myapp/product_form.html'


class Product_Update(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/product_form.html'


def product_delete(request, pk):
    if Product.objects.filter(pk=pk).delete():
        print('deleted')
    return request


def product_view(request, pk):
    context = {'product': Product.objects.get(pk=pk), 'admin_mode': True, 'title': 'Товар'}
    return TemplateResponse(request, 'myapp/product_view.html', context)


def index(request):
    context = {'homeworks': homeworks, 'title': 'Учебный проект по курсам Верстка, Flask, Django'}
    logger.info('Index page requested')
    return TemplateResponse(request, 'template_index.html', context)


def about(request):
    context = {'title': 'О себе, магазине, философии существования мира'}
    logger.info('About page requested')
    return TemplateResponse(request, 'about.html', context)


def shop_index(request):
    context = {'title': 'ДЗ№2 - Интернет-магазин'}
    context['links'] = [
        {'link': 'create_random_products/10', 'title': 'Нагенерить рандомных товаров'},
        {'link': 'create_random_users/10', 'title': 'Нагенерить рандомных юзеров'},
        {'link': 'catalog',
         'title': 'Просмотреть список категорий, добавить товары в корзину, создать новую категорию'},
        {'link': 'product/create', 'title': 'Создать товар'},
        {'link': 'users_list', 'title': 'Посмотреть юзеров и залогиниться'},
        {'link': 'into_deep', 'title': 'Посмотреть корзину залогиненного юзера'},
        {'link': 'all_orders', 'title': 'Посмотреть заказы залогиненного юзера'},
    ]
    return TemplateResponse(request, 'myapp/shop_adm_index.html', context)


def create_random_users(request, num=10):
    for i in range(num):
        c = Client(name=fake.name(), email=fake.email(), phone=fake.phone_number(), address=fake.address())
        c.save()
    return redirect('catalog')


def view_users(request):
    context = {'users': Client.objects.all(), 'title': 'Список пользователей'}
    return TemplateResponse(request, 'myapp/template_users.html', context)


def catalog(request, id=-1):
    if id == -1:
        categories = Category.objects.all()
        context = {'categories': categories,
                   'title': f'Список категорий:',
                   'can_create': True}
        response = render(request, 'myapp/cate_list.html', context)
    else:
        categories = Category.objects.filter(pk=id).first()
        products = Product.objects.filter(category_id=id)
        context = {'products': products,
                   'title': f'Товары в категории: {categories.cat_name}',
                   'cat_title': f'Товары в категории: {categories.cat_name}', }
        response = render(request, 'myapp/template_shop.html', context)
    return response


def create_random_products(request, num=10):
    if 1 < num > 10:
        num = 10
    for i in range(num):
        p_title = f'Рандомный товар {i}'
        p_descr = fake.text()
        cat = random.choice(Category.objects.all())
        img_link = 'noimage.jpg'
        p = Product(p_name=p_title, p_description=p_descr, price=random.randint(10, 100),
                    quantity=random.randint(5, 15), category_id=cat.id, image_link=img_link)
        p.save()
    return redirect('catalog')


def login_client(request, num):
    responce = redirect('catalog')
    responce.set_cookie('client_id', num)
    return responce


def into_basket(request, new_basket_product=False):
    id_client = int(request.COOKIES["client_id"])
    client = Client.objects.get(pk=id_client)
    order = Order.objects.filter(id_client=client, status='CR').first()
    if new_basket_product:  # если добавляется новый товар
        if not order:  # в новый заказ
            client.order_set.create(amount=1)
            order = client.order_set.last()
        product = Product.objects.get(pk=new_basket_product)
        product_in_order = order.orderdetail_set.filter(product_id=product).first()
        if product_in_order:
            product_in_order.quantity += 1
            product_in_order.save()
        else:
            order.orderdetail_set.create(quantity=1, product_id=product)
    order.amount = order.counting_amount()
    order.save()
    username = client.name
    context = {'title': f'Корзина для пользователя {username}',
               'quantity': order.orderdetail_set.values('quantity'),
               'summ': order.amount,
               'order': order.pk,
               'products': Product.objects.filter(orderdetail__order_id=order.id).values('id', 'p_name', 'price',
                                                                                         'orderdetail__quantity'), }
    return TemplateResponse(request, 'myapp/template_basket.html', context)


def del_product_from_basket(request, id_pr=False, id_order=False):
    if id_pr and id_order:
        id_client = int(request.COOKIES["client_id"])
        if id_client:
            OrderDetail.objects.filter(order_id=id_order, product_id=id_pr).delete()
            messages.add_message(request, messages.SUCCESS, 'Успешно')
    else:
        messages.add_message(request, messages.ERROR, 'Что-то смогло пойти не так')
        redirect('into_basket')
    return redirect('into_basket')


def confirm_order(request, id_order):
    Order.objects.filter(pk=id_order).update(status='CF')
    return redirect('all_orders')


def clear_order(request, id_order):
    Order.objects.filter(pk=id_order).exclude(status='CR').delete()
    return redirect('into_basket')


def cancel_order(request, id_order):
    Order.objects.filter(pk=id_order).update(status='CN')
    return redirect('all_orders')


def view_order(request, id_order):
    ps = Product.objects.filter(orderdetail__order_id_id=id_order)
    order = Order.objects.get(pk=id_order)
    context = {'products': ps,
               'status': order.status,
               'title': f'Заказ №{id_order} от {order.creating_date}',
               'summ': order.amount}
    return TemplateResponse(request, 'myapp/order_inside.html', context)


def all_orders(request):
    id_client = int(request.COOKIES["client_id"])
    if id_client:
        orders = Order.objects.filter(id_client=id_client).exclude(status='CR').values('id', 'creating_date', 'status')
        context = {'orders': orders,
                   'title': 'Список заказов'}
        response = TemplateResponse(request, 'myapp/orders_list.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Что-то смогло пойти не так')
        response = redirect('shop_index')
    return response


def products_list(request, time_select):
    id_client = int(request.COOKIES["client_id"])
    prs = Product.objects.filter(orderdetail__order_id__id_client=id_client)
    today = timezone.now()
    str_period = ''
    match time_select:
        case 'month':
            prs.filter(orderdetail__order_id__creating_date__gte=(timezone.now() - timezone.timedelta(days=365)))
            str_period = ' за месяц'
        case 'year':
            prs.filter(orderdetail__order_id__creating_date__gte=(timezone.now() - timezone.timedelta(days=30)))
            str_period = ' за год'
        case 'week':
            print('week')
            prs.filter(orderdetail__order_id__creating_date__gte=(timezone.now() - timezone.timedelta(days=7)))
            str_period = ' за неделю'
        case _:
            redirect('all_orders')
    context = {'products': prs,
               'title': f'Купленные товары {str_period}'}
    return render(request, 'myapp/product_list.html', context)


def delete_user(request, id_user):
    Client.objects.get(pk=id_user).delete()
    return redirect('users_list')
