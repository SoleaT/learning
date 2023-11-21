from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    cat_name = models.CharField(max_length=150)
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.cat_name


class Client(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    registration_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'

    def __str__(self):
        return self.name

    def count_orders(self):
        return Order.objects.filter(id_client=self.id).count()

class Product(models.Model):
    p_name = models.CharField(max_length=80)
    p_description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    adding_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image_link = models.ImageField(verbose_name='Product_', blank=True, default='noimage.jpg')
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse('product_view', args=[str(self.id)])



class Order(models.Model):
    class Statuses(models.TextChoices):
        CREATED = 'CR', _('Created')
        CONFIRMED = 'CF', _('Confirmed')
        PAID = 'PD', _('Paid')
        SHIPPED = 'SH', _('Shipped')
        CLOSED = 'CL', _('Closed')
        CANCELLED = 'CN', _('Cancelled')

    id_client = models.ForeignKey(Client, on_delete=models.PROTECT,verbose_name='Клиент')
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Количество')
    creating_date = models.DateField(auto_now_add=True,verbose_name='Дата создания заказа')
    change_status_date = models.DateField(auto_now=True,verbose_name='Дата изменения статуса')
    status = models.CharField(max_length=2, choices=Statuses.choices, default=Statuses.CREATED,verbose_name='Статус')

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def __str__(self):
        return str(self.creating_date)

    def counting_amount(self):
        summ = 0
        for item in self.orderdetail_set.all():
            p = Product.objects.filter(pk=item.product_id_id).first()
            if not p:
                continue
            p = p.price
            summ += item.quantity * p
        # summ =  Product.objects.filter(orderdetail__order_id=self.id).aggregate(models.Sum('price'))
        # summ = order.orderdetail_set.get(order_id=self.id).product.aggregate(models.Sum('price'))
        return summ


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
