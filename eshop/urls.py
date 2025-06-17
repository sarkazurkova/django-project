from django.urls import path
from . import views
#from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('zanry', views.zanry, name='zanry'),
    path('zanry/<int:pk>', views.zanr_detail, name='zanr_detail'),
    path('autori/', views.autori, name='autori'),
    path('autori/<int:pk>', views.autor_detail, name='autor_detail'),
    path('knihy', views.knihy, name='knihy'),
    path('knihy/<int:pk>', views.kniha_detail, name='kniha_detail')
]

   