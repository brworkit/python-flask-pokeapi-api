from application.utils import log, time, utils

class CategorySearchService(object):
    def __init__(self):
        pass

    def filter_by_search(self, search, items):
        print("filter_by_search")                
        items = self.apply_filter(search=search, items=items)
        items = sorted(items, key=lambda item: (-item['ratio'], item['name']))
        return items
       
    def apply_filter(self, search, items):
        log.i("apply_filter")
        log.i("search: {}".format(search))
        result = []
        search_lower = search.lower()
        for item in items:
            fields = [
                item["name"]                
            ]
            ratio = self.find_ratio(search_lower, fields)
            if ratio:
                item["ratio"] = ratio
                result.append(item)
        return result
    
    def find_ratio(self, search, fields):
        for field_value in fields:
            field_value = str(field_value).lower()
            if search in field_value:
                return utils.find_max_similarity(search=search, fields=fields)
        return 0.0