"""citycouncil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('overview.urls')),
    url(r'^admin/', admin.site.urls),
]
