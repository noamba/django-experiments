from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',
            views.index, name='index'),
        url(r'^setting_up_the_website$',
            views.setting_up_the_website, name='setting_up_the_website'),
        url(r'^top_brand_graph$',
            views.top_brand_graph, name='top_brand_graph'),
        url(r'^data_structures$',
            views.data_structures_and_cython,
            name='data_structures_and_cython'),
        url(r'^api/count_items_by_brand$',
            views.count_items_by_brand, name='count_items_by_brand'),
]
