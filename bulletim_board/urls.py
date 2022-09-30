from xml.etree.ElementInclude import include
from django.urls import path,include
from .import views

app_name ='bulletim_board'

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('list/',views.Bulletim_boardListView.as_view(), name="list"),
    path('create/',views.Bulletim_boardCreateView.as_view(), name="create"),
    # 9/29追加
    path('update/<int:pk>',views.UpdateView.as_view(),name="update"),
    path('delete/<int:pk>',views.DeleteView.as_view(),name="delete"),
    path('detail/<int:pk>/',views.DetailView.as_view(),name="detail"),
    path('mylist/',views.Bulletim_boardMyListView.as_view(),name="mylist"),
    path('my_detail/<int:pk>/',views.MyDetailView.as_view(),name="my_detail"),
    
]
