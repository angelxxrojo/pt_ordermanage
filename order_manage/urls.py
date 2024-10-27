from django.urls import path
from . import views

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('update-order/<int:order_id>/', views.update_order, name='update_order'),
]