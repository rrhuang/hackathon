from django.urls import path

from . import views

# from django.conf.urls import url
# from mysite.core import views as core_views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.signup),
    # path('handleSignup', views.handleSignup),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name = 'login'),
    path('success',views.success,name = 'success'),
    path('main_page', views.main_page, name='main_page'),
    path('send_money', views.send_money, name='send_money'),
    path('authauth', views.authauth, name='authauth'),
    path('successful', views.successful, name='successful')

    
]
