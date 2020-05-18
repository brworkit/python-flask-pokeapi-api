from application.utils import log


class CategoryPopulator(object):
    def __init__(self):
        pass

    def populate_minimum_response(self, items):
        log.i("populate_minimum_response")
        result = []
        for item in items:
            try:
                result.append({
                    "id": item["id"],
                    "name": item["name"],
                    "link": item["link"],
                    "urlName": item["urlName"],
                    "coupons": item["coupons"]})
            except Exception as e:
                print(f"Exception: {e}")
                print(f"item: {item}")

        return result
