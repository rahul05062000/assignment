from django.contrib import admin
from django.urls import path,include
from .import views 
from .views import GeneratePdf

urlpatterns = [
    path('',views.index,name='hii'),
    path('genarate_list',views.save_list,name='save_list'),
    path('view_list',views.show,name='view_list'),
    path('clear_prev',views.clear,name='clear_prev'),
    path('pdf', GeneratePdf.as_view()),
    # path('update',views.update,name='update'),

    
]