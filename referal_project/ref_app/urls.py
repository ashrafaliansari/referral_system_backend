from django.urls import path
from django.conf.urls import url
from .views import post2
from ref_app import views
urlpatterns =[
    # path('register',RegistrationView.as_view()),
    url('getdata',views.get_data),
    path('register2',views.post2),
]