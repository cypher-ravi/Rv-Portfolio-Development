from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from . views import home

urlpatterns = [
    path('super-secret-admin-atc-program/', admin.site.urls),
    # path('', home, name='home'),
    path('', include('core.urls',namespace='core')),

]
# handler500 = 'core.views.error_500'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__', include(debug_toolbar.urls))]