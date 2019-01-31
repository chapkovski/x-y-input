from django.conf.urls import url, include
from otree.urls import urlpatterns


urlpatterns.append(url(r'^captcha/', include('captcha.urls')), )
