from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('bathroom_selector/', views.bathroom_selector, name='bathroom_selector'),
    path('bathroom/<int:pk>', views.bathroom, name='bathroom'),

]
