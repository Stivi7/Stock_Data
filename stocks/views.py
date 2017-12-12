from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from django.template import RequestContext, Template

ts = TimeSeries(key='YDS2B660JTJ220OR', output_format='pandas')


def home(request):
    return render(request, 'stocks/home.html')


def stock_data(request):
    if request.method == 'POST':
        tag = request.POST['tag']
        data, meta_data = ts.get_daily(symbol=tag, outputsize='full')
        data['close'].plot()


        response = HttpResponse(content_type="image/png")
        plt.title('Daily Time Series for ' + tag)
        plt.savefig(response, format="png")
        return response


