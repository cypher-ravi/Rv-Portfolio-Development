from django.contrib import admin
from .models import Contact,Service,SubService,Testimonial

# Register your models here
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Testimonial)
