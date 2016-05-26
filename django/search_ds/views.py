from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404

from .models import Item


def show_ds(request):

    try:
        item_list = Item.objects.all()[:5]
    except:
        raise Http404("Problem getting items")

    context = {
        'item_list': item_list,
    }

    return render(request, 'search_ds/search_ds.html', context)


def show_ds_graph(request):

    id_list = []
    try:
        item_list = Item.objects.all()[:25]
    except:
        raise Http404("Problem getting items")

    for i in item_list:
        id_list.append(i.item_id)

    context = {
        'id_list': id_list,
    }

    return render(request, 'search_ds/search_ds_graph.html', context)


def count_items_by_brand(request):

    # data = Item.objects.all()[20]
    # data = [34, 65, 11]
    data = {"Prada": "34", "Levis": "65", "Next": "11"}
    return JsonResponse(data, safe=False)
