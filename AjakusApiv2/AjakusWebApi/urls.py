from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AjakusWebApi.views import ContentDetail,ContentList,UserDetail,UserList
from AjakusWebApi import views


urlpatterns = [

    path('contents/', views.ContentList.as_view()),
    path('contents/<int:pk>/', views.ContentDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)