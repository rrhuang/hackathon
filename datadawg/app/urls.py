from django.urls import path

from . import views

# from django.conf.urls import url
# from mysite.core import views as core_views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.signup),
    # path('handleSignup', views.handleSignup),
    path('signup/', views.signup, name='signup'),
    
]
