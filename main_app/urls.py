from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('list/', views.List.as_view(), name='list'),
  path('about/', views.about, name='about'),
  path('login/', views.Login.as_view(), name='loginuser'),
  path('signup/', views.signup, name='signup'),
  path('conspiracies/create', views.ConspiracyCreate.as_view(), name='conspiracy_create'),
  path('conspiracies/<int:pk>/update', views.ConspiracyUpdate.as_view(), name='conspiracy_update'),
  path('conspiracies/<int:pk>/delete', views.ConspiracyDelete.as_view(), name='conspiracy_delete'),
  path('conspiracies/<int:pk>/', views.conspiracy_detail, name='conspiracy_detail'),
  path('conspiracies/<int:pk>/addpic', views.add_pic, name='add_pic'),
]