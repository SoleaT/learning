from django.contrib import admin
from myapp.models import Category, Client, Product, Order


def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'quantity', 'category', 'price']
    ordering = ['price']
    list_filter = ['quantity', 'adding_date']  # небось, где-нибудь есть настройка по секторам, но не говорить же нам
    search_fields = ['p_name']
    search_help_text = 'Поиск по полю "имя продукта"'
    actions = [reset_quantity]
    fields = ['p_name', 'p_description', 'price', 'category', 'adding_date']
    readonly_fields = ['adding_date']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'count_orders']
    search_fields = ['name']
    search_help_text = 'Поиск по имени клиента:'
    readonly_fields = ['registration_date']


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['cat_name']
    search_help_text = 'Поиск по названию категории:'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['creating_date', 'id_client']
    ordering = ['client_id']
    list_filter = ['client_id','adding_date']
    fields = ['client_id', 'amount', 'creating_date', 'change_status_date']
    readonly_fields = ['creating_date', 'change_status_date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
