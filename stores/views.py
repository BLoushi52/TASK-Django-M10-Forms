from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import StoreItem
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
    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")
    context = {
        "form": form,
    }
    return render(request, 'create_store_item.html', context)

def update_store_item(request, item_id):
    item = StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=item)
    if request.method == "POST":
        form = StoreItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")
    context = {
        "item": item,
        "form": form,
    }
    return render(request, 'update_store_item.html', context)

def delete_store_item(request, item_id):
    StoreItem.objects.get(id=item_id).delete()
    return redirect("store-item-list")