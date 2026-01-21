# from django.urls import path
# from . import views

# urlpatterns = [
#     path('create_basket/', views.create_basket_view, name='create_basket'),
#     path('basket_list/', views.read_basket_view, name='basket_list'),
#     path('basket_list/<int:id>/update/', views.update_basket_view, name='update'),
#     path('basket_list/<int:id>/delete/', views.delete_basket_view, name='delete'),
# ]

from django.urls import path
from .views import (
    BasketCreateView,
    BasketListView,
    BasketUpdateView,
    BasketDeleteView
)

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view(), name='basket_create'),
    path('basket_list/', BasketListView.as_view(), name='basket_list'),
    path('basket_list/update/<int:pk>/', BasketUpdateView.as_view(), name='update'),
    path('basket_list/delete/<int:pk>/', BasketDeleteView.as_view(), name='delete'),
]
