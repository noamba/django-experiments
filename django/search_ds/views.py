from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from mysite.settings import NUMBER_OF_TOP_BRANDS_TO_CHART, BARS_IN_CHART

from .models import Brand


def index(request):

    return render(request, 'search_ds/index.html', '')


def top_brand_graph(request):
    """
    Renders a chart number of items per Brand.
    The Brand with most items is on top.
    """

    top_brands = Brand.objects.annotate(number_of_items=Count('item')).\
        order_by('-number_of_items')[:NUMBER_OF_TOP_BRANDS_TO_CHART]

    context = {
        'top_brands': top_brands,
        'bars_in_chart': BARS_IN_CHART,

    }

    return render(request, 'search_ds/top_brand_graph.html', context)


def count_items_by_brand(request):
    """
    Returns json of Brands and the number of items they have in the database.
    Only top brands are presented (ranked according to total items per brand).

    """

    # Create a list of dictionaries like:
    # {'brand': 'Simply Be', 'total': 4360}, ... ]
    top_brands_list_of_dicts = Brand.objects.values('name').\
        annotate(number_of_items=Count('item')).\
        order_by('-number_of_items')[:NUMBER_OF_TOP_BRANDS_TO_CHART]

    # to convert to json, need first to convert data into one dictionary:
    top_brands_dict =\
        {d['name']: d['number_of_items'] for d in top_brands_list_of_dicts}

    # JsonResponse will serialize a dict into json
    # and httpresponse it with the correct Content-Type header:
    # 'application/json'
    return JsonResponse(top_brands_dict)
