import random

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours.data import tours
from tours import data


def main_view(request):
    random_tours = dict(random.sample(tours.items(), 6))
    context = {
        "header": data.title,
        "subtitle": data.subtitle,
        "description": data.description,
        "departures": data.departures,
        "tours": random_tours
    }
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure):
    departure_name = data.departures[departure].replace("Из", "из")
    tours_list = {}
    for k, v in tours.items():
        if v['departure'] == departure:
            tours_list.update({k: v})
    prices = [price['price'] for price in tours_list.values()]
    nights = [night['nights'] for night in tours_list.values()]
    context = {
        "departures": data.departures,
        "departure": departure_name,
        "tours": tours_list,
        "pricemin": min(prices),
        "pricemax": max(prices),
        "nightmin": min(nights),
        "nightmax": max(nights),
    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, tour_id):
    context = {
        "tour": tours[tour_id],
        "departures": data.departures,
        "departure": data.departures[tours[tour_id]["departure"]].replace("Из", "из")
    }
    return render(request, 'tours/tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена. Зайдите попозже.')


def custom_handler500(request):
    return HttpResponseServerError('Сервер недоступен. Зайдите попозже.')
