from django.conf.urls import url
from .views import FoodListView, FoodDetailView, CartView

urlpatterns = [
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^(?P<category>[a-zA-Z0-9-]+)/$',
        FoodListView.as_view(), name='food_list'),
    url(r'^(?P<category>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/$',
        FoodDetailView.as_view(), name='food_detail')
]
