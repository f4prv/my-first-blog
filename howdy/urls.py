# howdy/urls.py
from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^about2/$', views.About2PageView.as_view()),

]


