from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve
from django.contrib.auth.views import LoginView
from .views import appuser_create_view, signup
from .views import question_create, question_update, question_delete, question_list, question_detail, QuestionDeleteView, signup, CustomLoginView
from django.contrib.auth import login

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('appuser/create/', appuser_create_view, name='appuser_create'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('question/add/', question_create, name='question_create'),
    path('question/<int:pk>/edit/', question_update, name='question_edit'),
    path('question/<int:pk>/delete/', question_delete, name='question_delete'),
    path('questions/', question_list, name='questions'),
    path('questions/<int:pk>/', question_detail, name='question_detail'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    path('signup/', signup, name='signup'),
    #path('login/', LoginView.as_view(template_name='guide_app/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # If you need a custom URL pattern for media files, it should look like this:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


