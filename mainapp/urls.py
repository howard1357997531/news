from django.urls import path
from mainapp import views2
from .views import guest, index, detail ,register, login, logout, accountsetting ,createnew, updatenew, deletenew

urlpatterns = [
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('',guest),
    path('index/',index),
    path('detail/<int:pk>/',detail),
    path('accountsetting/',accountsetting),
    path('createnew/',createnew),
    path('updatenew/<int:pk>/',updatenew),
    path('deletenew/<int:pk>/',deletenew),
]


urlpatterns += [
    path('guest_category1/',views2.guest_category1),
    path('guest_category2/',views2.guest_category2),
    path('guest_category3/',views2.guest_category3),
    path('guest_category4/',views2.guest_category4),
    path('guest_category5/',views2.guest_category5),
    path('guest_category6/',views2.guest_category6),
    path('guest_category7/',views2.guest_category7),

    path('index_category1/',views2.index_category1),
    path('index_category2/',views2.index_category2),
    path('index_category3/',views2.index_category3),
    path('index_category4/',views2.index_category4),
    path('index_category5/',views2.index_category5),
    path('index_category6/',views2.index_category6),
    path('index_category7/',views2.index_category7),
]

