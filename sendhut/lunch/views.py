from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item, Basket


class FoodListView(ListView):

    model = Item
    context_object_name = 'items'

    def get_queryset(self):
        category = self.kwargs['category']
        return Basket.filter_by_category_slugs([category])[:30]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category = self.kwargs['category']
        context['page_title'] = Basket.format_slug(category)
        return context


class FoodDetailView(DetailView):

    model = Item
    context_object_name = 'item'
    template_name = 'lunch/_item_detail.html'

    def get_object(self):
        # category_slug = self.kwargs['category']
        slug = self.kwargs['slug']
        return get_object_or_404(Item, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = context['item'].name
        return context
