from django.contrib import admin
from django.urls import path, include

from cafe.views import *
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    
    path('', index, name = 'index'),
    path('about-us', about, name = 'about-us'),

    #Function based views
    path('category/salad/', salad_list_api, name = 'salad'),
    path('category/salad/<int:salad_id>/', salad_item_api, name = 'singlesoup'),
    
    path('category/snack/', snack_list_api, name = 'snack'),
    path('category/snack/<int:snack_id>/', snack_item_api, name = 'singlesnack'),
    
    #path('category/salad/', salad_list_render, name = 'salad'),
    #path('category/salad/<int:salad_id>/', salad_item_render, name = 'singlesoup'),
    
    #path('category/snack/', snack_list_render, name = 'snack'),
    #path('category/snack/<int:snack_id>/', snack_item_render, name = 'singlesnack'),


    #path('category/dessert/', dessert_list, name = 'dessert'),
    #path('category/dessert/<int:dessert_id>/', dessert_item, name = 'singledessert'),
    #path('category/soup/', soup_list, name = 'soup'),
    #path('category/soup/<int:soup_id>/', soup_item, name = 'singlesoup'),


    #Сlass based views
    path('category/soup/', SoupListAPIView.as_view(), name = 'soup'),
    path('category/soup/<int:pk>/', SoupDetailAPIView.as_view(), name = 'singlesoup'),

    path('category/dessert/', DessertListAPIView.as_view(), name = 'dessert'),
    path('category/dessert/<int:pk>/', DessertDetailAPIView.as_view(), name = 'singledessert'),
    
    path('category/order/', OrderListAPIView.as_view(), name = 'order'),
    path('category/order/<int:pk>/', OrderDetailAPIView.as_view(), name = 'singleorder'),
    
    #path('category/soup/', SoupListRenderView.as_view(), name = 'soup'),
    #path('category/soup/<int:pk>/', SoupDetailRenderView.as_view(), name = 'singlesoup'),

    #path('category/dessert/', DessertListRenderView.as_view(), name = 'dessert'),
    #path('category/dessert/<int:pk>/', DessertDetailRenderView.as_view(), name = 'singledessert'),
    
    
    #path('category/salad/', SaladListAPIView.as_view(), name = 'salad'),
    #path('category/salad/<int:pk>/', SaladDetailAPIView.as_view(), name = 'singlesalad'),
    #path('category/snack/', SnackListAPIView.as_view(), name = 'snack'),
    #path('category/snack/<int:pk>/', SnackDetailAPIView.as_view(), name = 'singlesnack'),
]