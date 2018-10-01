"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .view import home_page,contact_page,about_page,login_page,register_page
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

#from product1.views import productlistview,product_list_view,productdetailview,product_detail_view, productfeaturedlistview,productfeatureddetailview,productdetailslugview

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name ='register'),
    path('bootstrap/', TemplateView.as_view(template_name="bootstrap/example.html")),
    path('product1/', include("product1.urls", namespace="product1")),
    path('search/', include("search.urls", namespace="search")),
    #path('product1/', productlistview.as_view()),
    #path('featured/', productfeaturedlistview.as_view()),
    #path('featured/<int:pk>/', productfeaturedlistview.as_view()),
    #path('product1-fbv/', product_list_view),
    #path('product1/<int:pk>/', productdetailview.as_view()),
    #path('product1/<slug:slug>/', productdetailslugview.as_view()),
    #path('product1-fbv/<int:pk>/', product_detail_view),
    path('admin/', admin.site.urls),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

