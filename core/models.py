from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    messages = models.TextField(max_length=500)
    phone = models.CharField(max_length=15,blank=True)
    is_through_atc = models.BooleanField(default=False,blank=True)
    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
