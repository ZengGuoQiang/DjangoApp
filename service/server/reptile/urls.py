from service.urls import path
from server.reptile import views as reptile

urlpatterns = [
    path('getTxt/',reptile.getTxt)
]
