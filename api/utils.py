import requests

from api.models import BudgetStatus

MODEL = BudgetStatus
URL = f'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data?filterstatus=ACTIVE'
MODEL_FIELD_CONFIG ={
    'code': 'code',
    'name': 'name',
    'parentcode': 'parentcode',
    'startdate': 'startdate',
    'enddate': 'enddate',
    'status': 'status',
    'budgtypecode': 'budgtypecode',
}


class ImporterDataToModelFromApi:
    PAGE_SIZE = 10
    PAGE_START = 1

    def __init__(self, model, url, field_config):
        self.model = model
        self.url = url + f'&pageSize={self.PAGE_SIZE}'
        self.field_config = field_config

    def get_data_from_page(self, page):
        url = self.url + f'&pageNum={page}'
        rjson = requests.get(url).json()
        return rjson

    def make_obj_dict(self, obj):
        obj_dict = dict()
        for field in self.field_config:
            if obj[field]:
                obj_dict[field] = obj[field]
        return obj_dict

    def parse_page(self, data):
        for elem in data:
            obj_dict = self.make_obj_dict(elem)
            parentcode = obj_dict.get('parentcode')
            if parentcode:
                try:
                    parent = self.model.objects.get(parentcode=parentcode)
                except self.model.DoesNotExist:
                    parent = self.model.objects.create(code=parentcode, name='NAN')
            else:
                parent = None
            obj_dict['parentcode'] = parent
            if code := obj_dict.get('code'):
                try:
                    self.model.objects.filter(code=code).update(**obj_dict)
                except self.model.DoesNotExist:
                    self.model.objects.create(**obj_dict)

    def parse_pages(self):
        response = self.get_data_from_page(self.PAGE_START)
        data = response['data']
        self.parse_page(data)
        page_count = response['pageCount']
        for page in range(2, page_count + 1):
            self.parse_page(self.get_data_from_page(page)['data'])
