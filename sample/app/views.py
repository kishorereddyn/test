from django.shortcuts import render

# Create your views here.
from app.models import Market
from django.http import HttpResponse
DEFAULT_DATA_URL = 'http://adunits.datawrkz.com/production/interview/data.json'
import json
import requests
import datetime

def results(request):
    #import pdb;pdb.set_trace()
    data = Market.objects.all().values()
    new_data = []
    for i in data:
        #import pdb;pdb.set_trace()
        i['date'] = i['date'].strftime('%d-%b-%Y')
        i['Turnover (Rs. Cr)'] = i.pop('turnover')
        i['Shares Traded'] = i.pop('shares_traded')
        i.pop('id')
        new_data.append(i)

    dump = json.dumps({"success": True, "data": new_data})
    return HttpResponse(dump, content_type='application/json')


def load_data(request):
    data = requests.get(DEFAULT_DATA_URL).json()
    for i in data:
        query = Market(date=datetime.datetime.strptime(i.get('Date'), '%d-%b-%Y'),
                       open=i.get('Open'), close=i.get('Close'),
                       high=i.get('High'), low=i.get('Low'),
                       shares_traded=i.get('Shares Traded'),
                       turnover=i.get('Turnover (Rs. Cr)'))
        query.save()
    dump = json.dumps({'success': True, 'results': 'Data loaded successfully'})
    return HttpResponse(dump, content_type='application/json')


def get_datetime_obj(date):
    return datetime.datetime.strptime(date, '%d-%m-%Y')


def open_price_more_than_close_price(request, date1, date2):
    date1 = get_datetime_obj(date1)
    date2 = get_datetime_obj(date2)
    data = Market.objects.filter(date__range=(date1, date2)).values()
    new_data = []
    for i in data:
        i['date'] = i['date'].strftime('%d-%b-%Y')
        i['Turnover (Rs. Cr)'] = i.pop('turnover')
        i['Shares Traded'] = i.pop('shares_traded')
        i.pop('id')
        open = i.get('open')
        close = i.get('close')
        if open > close:
            new_data.append(i)

    dump = json.dumps({"success": True, "data": new_data})
    return HttpResponse(dump, content_type='application/json')


def Average(lst):
    return sum(lst) / len(lst)


def avg_turnover(request, date1, date2):
    date1 = get_datetime_obj(date1)
    date2 = get_datetime_obj(date2)
    data = Market.objects.filter(date__range=(date1, date2)).values()
    turnover = []
    for i in data:
        turnover.append(i.get('turnover'))

    avg_turnover = Average(turnover)
    dump = json.dumps({'sucess': True, "Average Turnover": avg_turnover})
    return HttpResponse(dump, content_type='application/json')


def avg_high_low(request, date1, date2):
    date1 = get_datetime_obj(date1)
    date2 = get_datetime_obj(date2)
    data = Market.objects.filter(date__range=(date1, date2)).values()
    turnover = []
    for i in data:
        high = i.get('high')
        low = i.get('low')
        turnover.append(high-low)

    avg_turnover = Average(turnover)
    dump = json.dumps({'sucess': True, "Average High Low Value": avg_turnover})
    return HttpResponse(dump, content_type='application/json')
