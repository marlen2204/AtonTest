from django.shortcuts import render
from . import utils


def index(request):
    template = 'page.html'
    return render(request, template)


def calculate_exchange_rates(request):
    template = 'page.html'
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    currency = request.GET.get('cur')
    table = utils.get_currencies(start_date.split('-'), end_date.split('-'), currency)
    context = {
        'table': table,
        'start_date': start_date,
        'end_date': end_date,
        'currency': currency,

    }

    return render(request, template, context)
