from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('check/', views.chek.as_view()),
    path('checkmyoder/', views.chekmyorder.as_view()),
    path('orders/', views.OrdersList.as_view()),  
]