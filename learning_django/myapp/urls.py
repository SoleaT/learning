from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homework2/into_deep/<int:new_basket_product>', views.into_basket, name='into_basket'),
    path('homework2/into_deep/', views.into_basket, name='into_basket'),
    re_path(r'^homework2/category/create/$', views.CategoryCreate.as_view(), name='cat_create'),
    re_path(r'^homework2/category/update/(?P<pk>\d+)/$', views.CategoryUpdate.as_view(), name='cat_update'),
    re_path(r'^homework2/category/delete/(?P<pk>\d+)/$', views.CategoryDelete.as_view(), name='cat_delete'),
    path('homework2/catalog/<int:id>', views.catalog, name='catalog'),
    path('homework2/catalog', views.catalog, name='catalog'),
    path('homework2/all_orders', views.all_orders, name='all_orders'),
    path('homework2/confirm_order/<int:id_order>', views.confirm_order, name='confirm_order'),
    path('homework2/clear_order/<int:id_order>', views.clear_order, name='clear_order'),
    path('homework2/view_order/<int:id_order>', views.view_order, name='view_order'),
    path('homework2/cancel_order/<int:id_order>', views.cancel_order, name='cancel_order'),
    path('homework2/week_list', views.products_list, {'time_select': 'week'}, name='week_list'),
    path('homework2/month_list', views.products_list, {'time_select': 'month'},name='month_list'),
    path('homework2/year_list', views.products_list, {'time_select': 'year'},name='year_list'),
    path('homework2/users_list/', views.view_users, name='users_list'),
    path('homework2/create_random_users/<int:num>', views.create_random_users, name='random_users'),
    path('homework2/create_random_users/', views.create_random_users, name='random_users'),
    path('homework2/create_random_products/<int:num>', views.create_random_products, name='create_random_products'),
    path('homework2/create_random_products/', views.create_random_products, name='create_random_products'),
    re_path(r'^homework2/product/create/$', views.ProductCreate.as_view(), name='create_product'),
    re_path(r'^homework2/product/update/(?P<pk>\d+)/$', views.Product_Update.as_view(), name='update_product'),
    re_path(r'^homework2/product/delete/(?P<pk>\d+)/$', views.product_delete, name='delete_product'),
    re_path(r'^homework2/product/view/(?P<pk>\d+)/$', views.product_view, name='product_view'),
    path('homework2/', views.shop_index, name='shop_index'),
    path('homework1/', views.about, name='about'),
    path('login_as/<int:num>', views.login_client, name='login_as'),
    re_path(r'^homework2/delete_product/(?P<id_pr>\d+)/(?P<id_order>\d+)/', views.del_product_from_basket,
            name='delete_product'),
    path('homework2/delete_product/', views.del_product_from_basket, name='delete_product'),
    path('delete_user/<int:id_user>', views.delete_user, name='delete_user'),
    path('', views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)