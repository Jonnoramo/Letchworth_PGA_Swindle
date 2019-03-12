"""Letchworth_PGA_Swindle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from blog import views as blog_views
from home import views
from handicap import views as handicap_views
from leaguetable import views as leaguetable_views
from signup import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^members/$', accounts_views.get_users, name='members'),
    url(r'^member_detail/(?P<user_id>\d+)/$', accounts_views.get_user_details, name='member_detail'),
    url(r'^blog$', blog_views.post_list, name="post_list"),
    url(r'^blog/$', blog_views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_details, name="post_details"),
    url(r'^blog/post/$', blog_views.new_post, name='new_post'),

    url(r'^handicap/$', handicap_views.get_handicap, name='handicap'),
    url(r'^league/$', leaguetable_views.get_league, name='league'),
    url(r'^signup/$', views.get_signup, name='signup'),
    url('', include('home.urls')),
    url('', include ('handicap.urls')),
]
