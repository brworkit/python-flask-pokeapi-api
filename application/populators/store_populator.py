from application.utils import log


class StorePopulator(object):
    def __init__(self):
        pass

    def populate_minimum_response(self, items):
        log.i("populate_minimum_response")
        result = []
        for item in items:
            result.append({
                "id": item["id"],
                "name": item["name"],
                "image": item["image"],
                "link": item["link"],
                "urlName": item["urlName"],
                "coupons": item["coupons"]})
        return result
