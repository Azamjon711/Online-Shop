from django.shortcuts import render
from django.views import View
from .models import Product, Type


class ProductListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            products = Product.objects.all()
            context = {
                "porducts": products,
                "search": search,
            }
            return render(request, "main/index.html", context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {
                    "porducts": products,
                    "search": search,
                }
                return render(request, "main/index.html", context)
            else:
                return render(request, "main/404.html")

class TypeListView(View):
    def get(self, request):
        types = Type.objects.all()
        context = {
            "types": types,
        }
        return render(request, "main/index.html", context)




