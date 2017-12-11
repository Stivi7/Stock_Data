from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YDS2B660JTJ220OR', output_format='pandas')


def home(request):
    return render(request, 'stocks/home.html')


def stock_data(request):
    data, meta_data = ts.get_intraday(symbol='AMZN', interval='60min',outputsize='full')

    # response = HttpResponse(mimetype="image/png")
    # data['close'].plot(response, format="png")
    return response


