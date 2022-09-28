from xml.etree.ElementInclude import include
from django.urls import path,include
from .import views

app_name ='bulletim_board'

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('list/',views.Bulletim_boardListView.as_view(), name="list"),
    path('create/',views.CreateView.as_view(), name="create"),
]
