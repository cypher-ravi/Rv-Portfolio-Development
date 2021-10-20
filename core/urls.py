from django.urls import path,include
from .views import awareness_program_view 
# contact_form,
# getpdf

app_name = 'core'
urlpatterns = [
    # path('form/', contact_form, name='contact-form'),
    path('', awareness_program_view, name='awareness-through-code-program'),
    # path('download-resume/',getpdf,name="get-resume") 
]
