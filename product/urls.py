from django.contrib import admin
from django.urls import path,include
from product import views
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetails.as_view()),
    path('categories/<slug:category_slug>/',views.CategoryList.as_view()),
    path('products/search/',views.search),
    path('comments/', views.AddComments.as_view()),
    path('rating/<int:pk>/', views.Addrating.as_view()),
  
]
