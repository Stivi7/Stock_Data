from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from io import StringIO, BytesIO
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from .models import Stock




ts = TimeSeries(key='YDS2B660JTJ220OR', output_format='pandas')


def home(request):
    s = Stock.objects.all()
    return render(request, 'stocks/home.html', {'stocks': s})


def stock_data(request):
    if request.method == 'POST':
        tag = request.POST['tag']
        data, meta_data = ts.get_monthly(symbol=tag)
        data['close'].plot()
        f = BytesIO()
        plt.savefig(f, format='png')
        # file to be saved in database
        content_file = ImageFile(f)
        content_file.name = tag
        s_create = Stock.objects.create(name_tag=tag, chart_img=content_file)
        s_create.save()
        return redirect('home')




