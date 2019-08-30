
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'userModel'
urlpatterns = [
    url(r'^$',views.dashboard,name='dashboard'),
    #url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    #url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^users/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.user_email_detail,name='user_email_detail'),
]
