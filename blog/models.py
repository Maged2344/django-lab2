from email.mime import image
from django.db import models
from django.shortcuts import reverse
# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=30)
    Description	 =models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name


    def get_show_url(self):
        return reverse("products.show", kwargs={"id":self.id})

        # use this in the .hmtl ---> object.get_show_url


    def get_all_url(self):
        return reverse("main_page")


    def get_delete_url(self):
        # conver products.delete (url name ) to the crossponding route ---> /products/delete/{id}
        return reverse("products.delete", kwargs={"id":self.id})


    def get_edit_url(self):
        return reverse("products.edit", kwargs={"pk":self.id})