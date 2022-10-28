from django.urls import path
from . import views
# URL conf
urlpatterns =[ 
    path("", views.say_hello, name='index'),
    path('delete/<int:post_id>/',views.delete, name='delete')
]