from cProfile import label
import django_filters
from django_filters import CharFilter

from .models import *

class NewsFilter(django_filters.FilterSet):           #可以用內容裡的任何一字來當搜尋目標
    title = CharFilter(field_name='title',lookup_expr='icontains',label='Title')

    class Meta :
        model = News
        fields = ['title','date_created']