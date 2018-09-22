

from django.urls import path


from .views import productlistview,productdetailslugview

urlpatterns = [
   
    path('', productlistview.as_view()),
   
    path('<slug:slug>/', productdetailslugview.as_view()),
   
]  

