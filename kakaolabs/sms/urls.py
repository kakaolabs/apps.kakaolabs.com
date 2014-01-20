from django.conf.urls import patterns, url

from .category_api import CategoriesService, SubcategoryService


urlpatterns = patterns('',
    url(r'^v1/categories/$', CategoriesService.as_view()),
    url(r'^v1/subcategory/(?P<category_id>\w+)/$', SubcategoryService.as_view()),
)
