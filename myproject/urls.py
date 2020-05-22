from django.urls import path

from .views import PublisherList,PublisherDetail
app_name = 'myproject'
urlpatterns = [

    path('', PublisherList.as_view(),name='index'),

    path('<int:pk>/',PublisherDetail.as_view(),name = 'detail'),
    ]