from django.urls import path,include
from .views import contact_form,awareness_program_view

app_name = 'core'
urlpatterns = [
    path('form/', contact_form, name='contact-form'),
    path('awareness-through-code-program/', awareness_program_view, name='awareness-through-code-program')
]
