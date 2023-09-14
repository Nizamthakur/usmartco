from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from fastcasrt import settings
from home import views


from home import views
urlpatterns = [
    path('',views.home,name = "home"),
    path("shopView/",views.shop,name = "shop"),
    path("about/",views.about,name = "about"),
    path("services/",views.services,name = "services"),
    path("blog/",views.blog,name = "blog"),
    path("contact/",views.contact,name = "contact"),
    path("userView/",views.user,name = "user"),
    path("cartView/",views.cart,name = "cart"),
    path("details/<int:pk>/",views.viewProduct , name = 'viewProduct'),
    path("purchase/",views.purchase,name = "purchase"),
    path("contactReply/",views.contactReply,name = "contactReply"),
    path("blogDetails/<int:pk>/",views.blogDetails , name = 'blogDetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
