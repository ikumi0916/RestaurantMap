from django.views import generic
from .models import Store
from django.conf import settings

"""
■IndexList
「model」に設定したオブジェクトのhtmlを作成しておく必要がある
【例】
・オブジェクト名：Store
・作成が必要なHTML：store_list.html
"""
class IndexView(generic.ListView):
    model = Store
    paginate_by = 10

    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['api_key'] = settings.GOOGLEMAP_API_KEY

        return ctx
