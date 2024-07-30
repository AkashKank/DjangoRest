from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('insert', views.insertData.as_view(), name='insertData'),
    path('update/<id>', views.updateData.as_view(), name='updateData'),
    path('delete/<id>', views.deleteData.as_view(), name='deleteData'),
]
