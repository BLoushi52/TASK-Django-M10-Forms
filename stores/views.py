from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from stores import models
from .forms import StoreItemForm

def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)

def create_store_item(request):
    form = StoreItemForm()
    context = {
        "form": form,
    }
    return render(request, 'create_store_item.html', context)