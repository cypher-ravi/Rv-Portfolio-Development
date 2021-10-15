from django.urls import path,include
from .views import contact_form

app_name = 'core'
urlpatterns = [
    path('form/', contact_form, name='contact-form')
]
