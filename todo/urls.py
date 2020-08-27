from django.urls import path
from . import views

urlpatterns = [

    path('',views.todo,name="todo"),
    path('complete/<t_id>',views.addComplete,name='complete'),
    path('deletecomplete',views.delComplete,name='deletecomplete'),
    path('deleteall',views.delAll,name='deleteall')

]