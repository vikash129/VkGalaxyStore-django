from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='blog-index' ),
    # path('shop/',include('shop.urls')),
    # path('blog/', include('blog.urls')),
]