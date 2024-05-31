from empapp import views
from django.urls import path


urlpatterns = [
path('empapp/',views.index),
path('display/',views.display),
path('search',views.search),
path('empapp/<cid>/<oid>/<txt>',views.look)
]
