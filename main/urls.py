from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
    path('career/', views.career, name='career'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup_driver, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
]