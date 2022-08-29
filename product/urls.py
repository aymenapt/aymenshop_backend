
from django.urls import path
from product import views
urlpatterns = [
    path('latestproducts/', views.ProductList.as_view()),
    path('listcategory/', views.ListOfCategories.as_view()),
    path('productitem/<slug:category_slug>/<slug:product_slug>/',views.ProductDetails.as_view()),
    path('categories/<slug:category_slug>/',views.CategoryList.as_view()),
    path('products/search/',views.search),
    path('comments/', views.AddComments.as_view()),
    path('rating/<int:pk>/', views.Addrating.as_view()),
  
]
