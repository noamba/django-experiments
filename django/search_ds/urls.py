from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.show_ds, name='show_ds'),
        url(r'^graph$', views.show_ds_graph, name='show_ds_graph'),
        url(r'^api/count_items_by_brand$',
            views.count_items_by_brand, name='count_items_by_brand'),
]
