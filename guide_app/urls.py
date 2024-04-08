from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
from .views import appuser_create_view 
from .views import question_create, question_update, question_delete

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('appuser/create/', appuser_create_view, name='appuser_create'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('question/add/', question_create, name='question_create'),
    path('question/<int:pk>/edit/', question_update, name='question_edit'),
    path('question/<int:pk>/delete/', question_delete, name='question_delete'),
    
]
