from django.urls import path
from .views import home,single,aloqa




urlpatterns=[
    # path("avtolist", AvtoListView.as_view()),
    path('',home,name='saxifa'),
    path('aloqa/',aloqa,name='alo'),
    path('single/<slug:slug>/', single, name='page'),
]








