from django.conf.urls import include, url
from django.contrib import admin

from website.views import index_page
from maze_generation import urls as maze_generation_urls
from poem_per_day import urls as poem_per_day_urls

urlpatterns = []

urlpatterns.extend(maze_generation_urls.urlpatterns)
urlpatterns.extend(poem_per_day_urls.urlpatterns)

urlpatterns.append(url(r'^$', index_page))
