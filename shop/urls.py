from django.urls import path
from . import views

urlpatterns = [
      path('',views.home,name='shophome' ),
      path('about/',views.about,name='AboutUS' ),
      path('contact/',views.contact,name='shophomeindex' ),
      path('tracker/',views.tracker,name='shophomeindex' ),
      path('search/',views.search,name='search'),
      path('productview/',views.productview,name='productview'),
      path('checkout/',views.checkout,name='checkout'),
 ]