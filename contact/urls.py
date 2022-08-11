from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('', views.ContactView.as_view(), name="contact_form"),
    path('send/', views.SendEmailView.as_view(), name="send_message"),
]
