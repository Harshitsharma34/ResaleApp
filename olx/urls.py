
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views as user_views
from product import views


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('post_ad/',views.post_ad,name='post_ad'),
    path('products/', include('product.urls',namespace='products')),
    path('accounts/', include('account.urls')),
    path('register/',user_views.Register, name='register' ),
    #path('accounts/', include('account.urls',namespace='account')),
    
]
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


