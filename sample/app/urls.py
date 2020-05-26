from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all_results$', views.results, name='results'),
    url(r'^load_data$', views.load_data, name='load_data'),
    url(r'^open_price_more_than_close_price/(?P<date1>\d{2}-\d{2}-\d{4})/(?P<date2>\d{2}-\d{2}-\d{4})/$',
        views.open_price_more_than_close_price,
        name='open_price_more_than_close_price'),
    url(r'^avg_turnover/(?P<date1>\d{2}-\d{2}-\d{4})/(?P<date2>\d{2}-\d{2}-\d{4})/$',
        views.avg_turnover,
        name='avg_turnover'),
    url(r'^avg_high_low/(?P<date1>\d{2}-\d{2}-\d{4})/(?P<date2>\d{2}-\d{2}-\d{4})/$',
        views.avg_high_low,
        name='avg_high_low'),
]
