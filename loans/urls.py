from django.urls import path
from . import views

urlpatterns = [
    path('', views.loans, name='loans'),
    path('single-loan/<str:pk>', views.loan, name='single-loan'),
    path('add-loan', views.addLoan, name='add-loan'),
    path('update-loan/<str:pk>', views.updateLoan, name='update-loan'),
    path('delete-loan/<str:pk>', views.deleteLoan, name='delete-loan'),
    path('add-payment/', views.addPayment, name='add-payment'),
    path('register/', views.registerUser, name='register')
]