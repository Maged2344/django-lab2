from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product as Product
from django.views.generic.edit import UpdateView, CreateView
from .forms import ProductForm
# Create your views here.
def index(request):
    products = Product.objects.all()
    return  render(request, "blog/index.html", context={"products":products})



def show(request, id):
    product = Product.objects.get(pk=id)
    # return HttpResponse(product)
    print(product.get_show_url())
    return  render(request, "blog/show.html", context={"product":product})

def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("/")

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name ='blog/edit.html'
    success_url = "/"



class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name ='blog/create.html'
    success_url = "/"







