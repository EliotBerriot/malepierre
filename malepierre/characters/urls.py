# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url

from . import views

careers_patterns = [
    url(r'^$', views.CareerList.as_view(), name="index"),
]

talents_patterns = [
    url(r'^$', views.TalentList.as_view(), name="index"),
]

skills_patterns = [
    url(r'^$', views.SkillList.as_view(), name="index"),
]

urlpatterns = [
    url(r'^careers/', include(careers_patterns, namespace='careers')),
    url(r'^talents/', include(talents_patterns, namespace='talents')),
    url(r'^skills/', include(skills_patterns, namespace='skills')),
]
