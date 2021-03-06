from django.shortcuts import render

from sendhut.stores.models import Store


def home(request):
    stores = Store.featured.all()
    context = {
        'page_title': 'Home',
        'stores': stores
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'page_title': 'About Us'})


def faqs(request):
    return render(request, 'faqs.html', {'page_title': 'FAQs'})


def privacy(request):
    return render(request, 'privacy.html', {
        'page_title': 'Privacy Policy'
    })


def terms(request):
    return render(request, 'terms.html', {
        'page_title': 'Terms and Conditions'
    })
