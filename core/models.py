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


class Testimonial(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    enrolled_course = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})

class Service(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

class SubService(models.Model):
    title = models.TextField()
    service = models.ForeignKey("Service", on_delete=models.CASCADE,blank=True,null=True)


    

    class Meta:
        verbose_name = ("SubService")
        verbose_name_plural = ("SubServices")

    # def __str__(self):
    #     return self.id

    def get_absolute_url(self):
        return reverse("SubService_detail", kwargs={"pk": self.pk})



