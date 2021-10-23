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
handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'


