
from django.urls import path
from product import views
urlpatterns = [
    path('latestproducts/', views.ProductList.as_view()),
    path('listcategory/', views.CategoryList.as_view()),
    path('ads/', views.ListOfAds.as_view()),
    path('productitem/<slug:product_slug>/',views.ProductDetails.as_view()),
    path('listofallproducts/',views.ListOfAllProducts.as_view()),
    path('products/search/',views.search),
    path('comments/', views.AddComments.as_view()),
    path('rating/<int:pk>/', views.Addrating.as_view()),
  
]
