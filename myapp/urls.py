from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
   url(r'^hello/', views.hello, name = 'hello'),
#   url(r'^morning/', views.morning, name = 'morning'),
   url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
   url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name = 'articles'),
   url(r'^crudops/', views.crudops, name = 'crud'),
   url(r'^datamanipulation/', views.datamanipulation, name ='datamanipulation'),
   url(r'^connection/', TemplateView.as_view(template_name = 'login.html')),
   url(r'^login/', views.login, name='login'),
              ]
