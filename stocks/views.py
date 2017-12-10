from django.shortcuts import render
import quandl
import json
from django.http import HttpResponse, JsonResponse

quandl.ApiConfig.api_key = "Yjg7ga--NqWsbtf6d4kb"

def stock_data(request):
    data = quandl.get("WIKI/AMZN", returns='json')
    print(data)
    data_array = []


    return JsonResponse(data_array, safe=False)
