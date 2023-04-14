from django.urls import path
from . import views

app_name = 'landingpage'

urlpatterns = [
    path('', views.home, name='home'),
    path('bio_page', views.bioPage, name='bio_page'),
    path('editing_page', views.editingPage, name='editing_page'),
    path('welding_page', views.weldingPage, name='welding_page'),
    path('drink_page', views.drinkPage, name='drink_page'),
    path('blog_page', views.blogPage, name='blog_page'),
    path('actual_blog_page', views.actualBlogPage, name='actual_blog_page'),
]


