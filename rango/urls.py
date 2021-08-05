from django.urls import path
from django.conf.urls import url
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('search/',views.search,name='search'),
    path('search/dessert_search'),
    path('search/article_search'),
    path('search/shop_search'),
    path('likelist'),
    path('likelist/<user_name>'),
    path('article'),
    path('shop'),
    path('shop/<shop_id>'),
]